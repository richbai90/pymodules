from metavision_hal import DeviceDiscovery
from common.observer import Subject, Observer
from typing import Tuple
from threading import Thread, Timer, Event


def get_biases_from_file(path: str):
    """
    Helper function to read bias from a file
    """
    biases = {}
    try:
        biases_file = open(path, 'r')
    except IOError:
        print("Cannot open bias file: " + path)
    else:
        for line in biases_file:

            # Skip lines starting with '%': comments
            if line.startswith('%'):
                continue

            # element 0 : value
            # element 1 : name
            split = line.split("%")
            biases[split[1].strip()] = int(split[0])
    return biases


def save_biases_to_file(path: str, biases: dict):
    """
    helper function to write biases to file
    """
    try:
        f = open(path, 'w')
    except IOError:
        print("Cannot save bias file: " + path)
    else:
        for name, value in biases.items():
            f.write(str(value) + " % " + name + "\n")


class EventCamera(Subject, Observer):
    def __init__(self, config=None) -> None:
        Subject.__init__(self) # Call the parent constructor
        Observer.__init__(self) # Call the parent constructor
        self._device = None
        self.streaming = False
        self._roi = (0, 0, 640, 480)
        self._biases = self.biases = {
                    'bias_diff': 299,
                    'bias_diff_off': 221,
                    'bias_diff_on': 384,
                    'bias_fo': 1477,
                    'bias_hpf': 1448,
                    'bias_pr': 1250,
                    'bias_refr': 1500
                } # Default biases as per metavision documentation
        
        self._config = config
        self._recording_thread = None

    def connect(self):
        if self._config is None:
            device = DeviceDiscovery.open('')
        else:
            device = DeviceDiscovery.open('', self._config)
        if device is not None:
            self._device = device
            self._set_roi()
            self._apply_biases()

    @property
    def hw_identification(self):
        return self._device.get_i_hw_identification()
    @property
    def base_path(self):
        "camera" + self.hw_identification.get_serial()
    @property
    def sensor_info(self):
        return self.hw_identification.get_sensor_info()
    @property
    def _geometry(self):
        return self._device.get_i_geometry()
    @property
    def device(self):
        return self._device
    @property
    def _device_roi(self):
        return self._device.get_i_roi()
    @property
    def _device_biases(self):
        return self._device.get_i_ll_biases()
    @property
    def stream(self):
        return self.device.get_i_events_stream()
    @property
    def _stream_decoder(self):
        return self.device.get_i_events_stream_decoder()
    @property
    def cd_decoder(self):
        return self.device.get_i_event_cd_decoder()
    @property
    def monitor(self):
        return self.device.get_i_monitoring()

    @property
    def biases(self):
        return self._biases
    
    @biases.setter
    def biases(self, biases):
        # check if biases is a string
        if isinstance(biases, str):
            self.set_biases_from_file(biases)
        else:
            self.set_biases(biases)

    @property
    def roi(self):
        return self._roi

    @roi.setter
    def roi(self, roi: Tuple[int, int, int, int]):
        '''
        Set the region of interest (ROI) of the camera.
        The ROI is a tuple of 4 integers (x, y, width, height).
        '''
        self._roi = roi
        self._set_roi() # Set the ROI on the device

    @property
    def device(self):
        return self._device

    @property
    def bias_range_check(self):
        return self._device.get_i_ll_biases_range_check_bypass()

    def get_size(self):
        return self._geometry.get_height(), self._geometry.get_width()
    
    def get_height(self):
        return self._geometry.get_height()
    
    def get_width(self):
        return self._geometry.get_width()

    def _get_device_biases(self):
        return self._device.get_i_ll_biases()

    def set_biases(self, biases):
        for bias_name, bias_value in biases.items():
            self.biases[bias_name] = bias_value
        if self._device is not None:
            self._apply_biases()

    def set_biases_from_file(self, bias_file):
        biases = get_biases_from_file(bias_file)
        self.set_biases(biases)

    def _apply_biases(self):
        device_biases = self._get_device_biases()
        for bias_name, bias_value in self.biases.items():
            device_biases.set(bias_name, bias_value)

    def _set_roi(self):
        device_roi = self._device_roi
        if not self.roi:
            return
        x0, y0, width, height = self.roi
        window = device_roi.Window(x0, y0, width, height)
        device_roi.set_window(window)
        device_roi.enable(True)

    def increase_bias(self, bias_name, amount=3):
        self.biases[bias_name] += amount
        self._apply_biases()

    def decrease_bias(self, bias_name, amount=3):
        self.biases[bias_name] -= amount
        self._apply_biases()
    
    def start_stream(self):
        self.streaming = True
        self.stream.start()
    
    def stop_stream(self):
        self.streaming = False
        self.stream.stop()
    
    def start_recording(self):
        self.notify_observers({'message_type': 'recording', 'message': 'starting'})
    
    def log_raw(self, log_path):
        self.stream.log_raw_data(log_path)
    
    def stop_log_raw(self):
        self.stream.stop_log_raw_data()
        
        
    def stop_recording(self):
        self.notify_observers({'message_type': 'recording', 'message': 'stopping'})
    
    def update(self, message):
        if message['message_type'] == 'recording':
            if message['message'] == 'start':
                self.recording = True
                self._recording_thread = Thread(target=self._record_events) # Create a new thread to record events
                self._recording_thread.start()
                self.notify_observers({'message_type': 'recording', 'message': 'started'})
            elif message['message'] == 'stop':
                self.recording = False
                self._recording_thread.join() if self._recording_thread is not None else None # Wait for the recording thread to finish 
                self._recording_thread = None
                self.stream.stop_log_raw_data() # Stop logging raw data to file always. Does nothing if not logging
                self.notify_observers({'message_type': 'recording', 'message': 'stopped'})
        elif message['message_type'] == 'record_raw':
                self.stream.log_raw_data(message['message']) # Log raw data to file
        
    def _record_events(self):
        while self.recording:
            data = self.stream.get_latest_raw_data()
            if data is not None:
                self._stream_decoder.decode(data)
            
    
        
if __name__ == '__main__':
    from time import sleep
    from threading import Timer
    camera = EventCamera()
    camera.connect()
    camera.start_stream()
    camera.log_raw('test.raw')
    monitor = camera.monitor
    for i in range(10):
        sleep(1)
        print(monitor.get_illumination())
        sleep(1)


