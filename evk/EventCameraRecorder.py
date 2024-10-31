import numpy as np
from common.observer import Observer, Subject
import pandas as pd
from . import EventCamera

class EventCameraRecorder(Observer, Subject):
    def __init__(self, camera: EventCamera.EventCamera, filename: str):
        super().__init__()
        self.camera = camera
        self.filename = filename
        self.save = None
        self.recording = False
        self.f = None
        self.file_type = self.filename.split('.')[-1]
        self._select_save_fn()
        self.camera.add_observer(self) # Listen for messages from the camera
        self.add_observer(self.camera) # Forward messages to the camera
        self.camera.cd_decoder.add_event_buffer_callback(self.save) # Listen for messages from the cd decoder
                
            
        
    def _select_save_fn(self):
        if self.file_type == 'txt':
            self.save = self._save_txt
        elif self.file_type == 'bin':
            self.save = self._save_bin
        elif self.file_type == 'csv':
            self.save = self._save_csv
        elif self.file_type == 'db':
            self.save = self._save_db
        elif self.file_type == 'raw':
            self.save = lambda _: None # Do nothing
        else:
            raise ValueError('Unknown file type: {} from file {}'.format(self.file_type, self.filename))
    
    def _start_recording(self):
        if self.save is None:
            raise RuntimeError('No save method specified')
        if self.file_type == 'csv':
            df = pd.DataFrame(columns=['x', 'y', 'polarity', 'timestamp'])
            df.to_csv(self.filename, index=False, lineterminator='\n')
            self.f = open(self.filename, 'a')
        elif self.file_type == 'db':
            import sqlite3
            conn = sqlite3.connect(self.filename)
            c = conn.cursor()
            c.execute('''CREATE TABLE events (timestamp real, x integer, y integer, polarity integer)''')
            conn.commit()
            conn.close()
        elif self.file_type == 'bin':
            f = open(self.filename, 'wb')
            f.close()
            self.f = open(self.filename, 'ab')
            
        elif self.file_type == 'txt':
            f = open(self.filename, 'w')
            f.close()
            self.f = open(self.filename, 'a')
        elif self.file_type == 'raw':
            self.notify_observers({'message_type': 'record_raw', 'message': self.filename})
        

        self.notify_observers({'message_type': 'recording', 'message': 'start'})
    
    def _stop_recording(self):
        # TODO: Add any pre stop recording actions here
        self.notify_observers({'message_type': 'recording', 'message': 'stop'})
        
    
    def _post_start_recording(self):
        # TODO: Add any post start recording actions here
        pass
    
    def _post_stop_recording(self):
        if self.f is not None:
            self.f.close()
        
        
    def update(self, message):
        if message['message_type'] == 'recording':
            if message['message'] == 'starting':
                self._start_recording()
            elif message['message'] == 'stopping':
                self._stop_recording()
            elif message['message'] == 'started':
                self._post_start_recording()
            elif message['message'] == 'stopped':
                self._post_stop_recording()
        
        

    def _save_txt(self, events: np.ndarray):
        np.savetxt(self.f, events)
    
    def _save_bin(self, events: np.ndarray):
        events.tofile(self.f) 
    
    def _save_csv(self, events: np.ndarray):
        df = pd.DataFrame(events, columns=['x', 'y', 'p', 't'])
        try:
            df.to_csv(self.f, header=False, index=False, lineterminator='\n')
        # catch the error if the file is closed
        except ValueError:
            # if the file closed before all the events were written, open the file again and write the remaining events
            f = open(self.filename, 'a')
            df.to_csv(f, header=False, index=False, lineterminator='\n')
            f.close()
    
    def _save_db(self, events: np.ndarray):
        import sqlite3
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.executemany('INSERT INTO events VALUES (?,?,?,?)', events)
        conn.commit()
        conn.close()
        
if __name__ == '__main__':
    from time import sleep
    from threading import Timer
    from evk.EventCamera import EventCamera
    camera = EventCamera()
    camera.connect()
    recorder = EventCameraRecorder(camera, 'test.csv')
    recorder2 = EventCameraRecorder(camera, 'test.raw')
    camera.start_recording()
    camera.start_stream()
    Timer(10, camera.stop_stream).start() # Stop streaming after 10 seconds
    
    while camera.streaming:
        pass
    
    camera.stop_recording()