from nkt_tools.extreme import Extreme
from threading import Thread, Event
import time
import logging

class Pulser():
    '''
    Pulser class for the NKT Extreme laser.
    
    Pulser class uses PWM to pulse the laser at a given frequency and pulse width.
    
    Parameters
    ----------
    laser : Extreme
    '''
    def __init__(self, laser: Extreme) -> None:
        '''
        Create a new Pulser object.
        '''
        logging.basicConfig(level=logging.INFO)
        self.laser = laser
        self._frequency = 100 * 1e-9 # GHz
        self._pulse_width = 100 # us
        self._calculate_off_time()
        self._started = Event()
        self._stop = Event()
        self._thread = None
        
        self._stop.set() # Always start with the laser off
        self._started.clear() # Always start with the laser off
        laser.set_emission(False) # Always turn off the laser on init
    
    def _calculate_off_time(self):
        '''
        Calculate the off time of the laser.
        The off time is the time between pulses.
        '''
        T = 1 / self._frequency # ns
        t_on = self._pulse_width * 1e3 # ns
        self._off_time = T - t_on
    
    @property
    def frequency(self):
        '''
        The frequency of the laser in Hz.
        '''
        return self._frequency / 1e-9 # Convert to Hz
    
    @frequency.setter
    def frequency(self, frequency):
        '''
        Set the frequency of the laser in Hz.
        '''
        if self._started.is_set():
            raise Exception('Cannot set frequency while laser is running.')
        self._frequency = frequency * 1e-9 # Convert to GHz
        self._calculate_off_time()
    
    @property
    def pulse_width(self):
        '''
        Pulse width of the laser in us.
        '''
        if self._started.is_set():
            raise Exception('Cannot set pulse width while laser is running.')
        return self._pulse_width / 1e3 # Convert to us
    
    @pulse_width.setter
    def pulse_width(self, pulse_width):
        '''
        Set the pulse width of the laser in us.
        '''
        self._pulse_width = pulse_width * 1e3 # Convert to ns
        self._calculate_off_time()
    
    def start(self, power: float = 14):
        '''
        Start the laser and pulse it at the given frequency and pulse width.
        '''
        logging.info("Starting")
        if self._started.is_set():
            return
        self.laser.set_mode(1)
        self.laser.set_power(power)
        self._stop.clear()
        self._thread = Thread(target=self._pulse)
        self._started.set()
        self._thread.start()
    
    def stop(self):
        '''
        Stop the laser.
        '''
        logging.info("Stopping")
        self.laser.set_emission(False) # Always turn off the laser
        if not self._started.is_set():
            return
        self._stop.set()
        self._thread.join()
        
    def _pulse(self):
        '''
        Pulse the laser in a loop until stop is called.
        
        Note: This function should not be called directly. Call start instead.
        Calling this function directly will cause the program to hang.
        '''
        while not self._stop.is_set():
            t = time.perf_counter_ns()
            self.laser.set_emission(True)
            logging.info("Pulse On")
            while(time.perf_counter_ns() - t < self._pulse_width * 1e6):
                pass
            self.laser.set_emission(False)
            logging.info("Pulse Off")
            while(time.perf_counter_ns() - t < self._off_time * 1e6):
                pass
        self._started.clear()
            
        
        
def test():
    laser = Extreme()
    laser.set_mode(1)
    laser.set_power(14)
    pulser = Pulser(laser)
    pulser.frequency = 10 # Hz
    pulser.pulse_width = 1e6 # us
    pulser.start()
    time.sleep(120) # Run for 2 minutes
    pulser.stop()
    
if __name__ == '__main__':
    test()