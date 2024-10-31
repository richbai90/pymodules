from metavision_core import event_io
import numpy as np
import logging
from typing import Callable
import time
import threading
import re

def _time_us() -> int:
    return int(time.time_ns() / 1000)

class EventProcessor:
    def __init__(self, reader: event_io.RawReader, reset=False, logger=None) -> None:
        self.pipeline = []
        self.integrate = False
        self.reader = reader
        self.reading = threading.Event()
        self.timer = None
        if logger is None:
            self.logger = logging.getLogger(f"__main__.{self.__class__.__name__}")
            # Create a new handler with a custom format (includes class name)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [{}] - %(message)s'.format(self.__class__.__name__))
            handler.setFormatter(formatter)
        else:
            self.logger = logger

        if reset:
            self.reader.reset()
    @property
    def count(self) -> int:
        return int(self._count())
            
    def _count(self):
        while(not self.reader.is_done()):
            self.reader.seek_event(100)
        
        n = self.reader.current_event_index()
        self.reader.reset() # Reset the reader
        return n
            
    def flush(self) -> None:
        tik = _time_us()
        current_time = _time_us()
        while not self.reader.is_done() and current_time - tik < 5e6:
            current_time = _time_us()
            logging.info(f"Flush: start time: {tik} current time: {current_time} time left: f{5e6 - current_time - tik}")
            self.reader.load_n_events(100)
            time.sleep(500e-6) # sleep for 500us
            
    def get_all_events(self, offset: int = 0) -> np.ndarray:
        self.reader.reset()
        if type(offset) is int:
            self.reader.seek_event(offset)
        elif type(offset) is str:
            rexp = re.compile(r'(\d+)\s?(\w+)')
            t, unit = rexp.findall(offset)[0]
            if unit == 's':
                t = int(t) * 1e6
            elif unit == 'ms':
                t = int(t) * 1e3
            elif unit == 'us':
                t = int(t)
            else:
                raise ValueError(f"Invalid unit: {unit}")
            self.reader.seek_time(t)
        while not self.reader.is_done():
            yield self.reader.load_n_events(1000) # Load 1000 events at a time
    
    def load_events(self, n: int) -> (np.ndarray, bool):
        events = self.reader.load_n_events(n)
        return self._process_pipeline(events)
    
    def load_events_for_duration(self, duration_us: int) -> (np.ndarray, bool):
        self.reading.set() # Set the reading flag
        self._start_timer(duration_us * 2 / 1e6, self._stop_reading) # Clear the reading flag after 2x the duration (timeout)
        events = []
        while self.reading.is_set():
            evts = self.reader.load_delta_t(duration_us)
            if len(evts) > 0:
                events.append(evts)
                break
        if self.reading.is_set():
            self.cancel()
        if len(events):    
            return self._process_pipeline(np.concatenate(events))
        return np.array([], dtype=dict), False # Return an empty array if no events were loaded
        
        if len(events) == 0:
            # try to load n events
            self._start_timer(duration_us / 1e6, self._stop_reading)
            events.append(self.reader.load_n_events(100))
        
        if len(events) == 0:
            return np.array([], dtype=dict), False # Return an empty array if no events were loaded
        
        
        
        return self._process_pipeline(np.concatenate(events))
    
    def _process_pipeline(self, arr: np.ndarray) -> (np.ndarray, bool):
        passed_pipeline = True
        
        for i, stage in enumerate(self.pipeline):
            next_frame = stage(arr, self.reader.current_time)
            # If the stage returns None, stop the pipeline and return the current frame
            if next_frame is None:
                passed_pipeline = False
                break
            # check if next_frame is an np.ndarray
            # this is so we can have stages that stop the pipeline without returning a frame
            elif not isinstance(next_frame, np.ndarray):
                next_frame = arr # If not, keep the current frame
            
            arr = next_frame
        return arr, passed_pipeline
        
    
    def produce_frame(self, start_ts: int = -1, delta_t: float = 10e3, show_progress: bool = False) -> (np.ndarray, bool):
        if start_ts != -1:
            self.reader.seek(start_ts)
        events = self.reader.load_delta_t(int(delta_t))
        frame = self.events_to_matrix(events)
        return self._process_pipeline(frame)
    
    def events_to_matrix(self, events: np.ndarray) -> np.ndarray:
        if len(events) == 0:
            return np.zeros((480, 640, 2), dtype=np.float32)
        # Extract x, y, p values from the events
        x_values = np.array([event['x'] for event in events])
        y_values = np.array([event['y'] for event in events])
        p_values = np.array([event['p'] for event in events])

        # Create a 3D matrix initialized with zeros
        matrix = np.zeros((480, 640, 2), dtype=np.float32)

        if self.integrate:
            np.add.at(matrix, (y_values, x_values, p_values), 1)
            matrix /= matrix.max() # normalize
            return matrix
        # Use advanced indexing to populate the matrix
        matrix[y_values, x_values, p_values] = 1
        return matrix
    
    def add_pipeline_stage(self, stage: Callable[[np.ndarray, int], np.ndarray]) -> int:
        idx = len(self.pipeline)
        self.pipeline.append(stage)
        return idx
    
    def remove_pipeline_stage(self, idx: int) -> None:
        self.pipeline.pop(idx)
        
    def process_all(self, dt: int = 0) -> None:
        while not self.done():
            if dt > 0:
                self.produce_frame(delta_t=dt)
            else:
                self.produce_frame()
    def process_until(self, ts: int, dt: int = 0) -> None:
        while not self.done() and self.reader.current_time < ts:
            if dt > 0:
                self.produce_frame(delta_t=dt)
            else:
                self.produce_frame()
    
    def process_until_event(self, event: int, dt) -> None:
        while not self.done() and self.reader.current_event_index < event:
            if dt > 0:
                self.produce_frame(delta_t=dt)
            else:
                self.produce_frame()
                
    def process_n_frames(self, n: int, dt: int = 0, pass_pipeline: bool = False) -> None:
        passed_pipeline = False
        for _ in range(n):
            while(not passed_pipeline and not self.done()):
                if dt > 0:
                    _, passed_pipeline = self.produce_frame(delta_t=dt)
                else:
                    _, passed_pipeline = self.produce_frame()
                if not pass_pipeline:
                    break
                
        
    def done(self) -> bool:
        try:
            return self.reader.is_done()
        except:
            return False
    
    def _start_timer(self, time, cb: Callable) -> None:
        self.timer = threading.Timer(time, cb)
        self.timer.start()
    
    def _stop_reading(self) -> None:
        logging.info("Stopping reading")
        self.reader._decode_done = True # Stop the reader from loading events
        self.reading.clear() # Clear the reading flag
        time.sleep(1) # Wait for the reader to finish loading events
        self.reader._decode_done = False # Reset the reader
    
    def cancel(self) -> None:
        self.timer.cancel()
        self._stop_reading()
    

if __name__ == "__main__":
    # Test
    import matplotlib.pyplot as plt
    from scipy.signal import fftconvolve
    from evk.EventCamera import EventCamera
    
    class Averager:
        def __init__(self, shape=(480,640,2), min_count=10) -> None:
            self.shape = shape
            self.min_count = min_count
            self._reset()
        def __call__(self, frame: np.ndarray, ts: int) -> np.ndarray:
            self.frames.append(frame)
            if len(self.frames) < self.min_count:
                return None
            matrix = np.mean(self.frames)
            self._reset()
            return matrix
        def _reset(self) -> None:
            self.frames = []
    
    class Threshold:
        def __init__(self, radius: int = 5, threshold=5) -> None:
            self.radius = radius
            self.x, self.y = np.ogrid[-radius: radius+1, -radius: radius+1]
            self.circular_mask = self.x**2 + self.y**2 <= radius**2
            self.threshold = threshold
        
        def __call__(self, frame: np.ndarray, ts: int) -> np.ndarray:
            result = fftconvolve(frame, self.circular_mask, mode='same')
            threshold_mask = (frame == 1) & (result < self.threshold)
            frame[threshold_mask] = 0
            return frame
    
    class ROIFilter:
        def __init__(self, x: int, y: int, width: int, height: int) -> None:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def __call__(self, frame: np.ndarray, ts: int) -> np.ndarray:
            return frame[self.y:self.y+self.height, self.x:self.x+self.width]
    


    reader = event_io.RawReader('test.raw')
    processor = EventProcessor(reader)
    # crop the frame to the center 115x115
    processor.add_pipeline_stage(ROIFilter(260, 180, 120, 120))
    processor.add_pipeline_stage(lambda x, _: x[:, :, 0])
    processor.add_pipeline_stage(Threshold(radius=5, threshold=5))
    processor.add_pipeline_stage(Averager(shape=(115, 115), min_count=100))
    processor.add_pipeline_stage(lambda x, ts: plt.imsave(fr'C:\Users\User\Documents\Rich Baird\test\{ts}.jpg', x, cmap='gray'))
    processor.integrate = True
    processor.process_n_frames(n=100, dt=5e3)
    
    
            