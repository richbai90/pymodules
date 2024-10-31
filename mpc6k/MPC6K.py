import serial

class Controller:
    """
    A class to interface with a laser PSU through a serial connection.
    """
    
    def __init__(self, port):
        """
        Initializes the serial connection with the specified port settings.
        
        Args:
            port (str): The port name to which the PSU is connected.
        """
        self.ser = serial.Serial(
            port=port,
            baudrate=19200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        
        print(self.send_command("VERSION?"))  # Print the PSU version information

    def send_command(self, command):
        """
        Sends a command to the PSU and returns the response.

        Args:
            command (str): The command to send.

        Returns:
            str: The response from the PSU.
        """
        self.ser.write((command + '\r\n').encode('utf-8'))
        response = self.ser.readline().decode('utf-8').strip()
        return response

    def turn_off(self):
        """Disables the laser, regardless of the interlock status."""
        return self.send_command("OFF")

    def turn_on(self):
        """Enables the laser subject to Interlock and Enable Switch status."""
        return self.send_command("ON")

    def set_control_current(self):
        """Sets the current mode on."""
        return self.send_command("CONTROL=CURRENT")

    def set_control_power(self):
        """Sets the power mode on."""
        return self.send_command("CONTROL=POWER")

    def set_current(self, percentage):
        """
        Sets the current to the diodes as a percentage of the maximum.

        Args:
            percentage (int): The percentage of the maximum current to set.
        """
        return self.send_command(f"CURRENT={percentage}")

    def set_power(self, power_mw):
        """
        Sets the output power of the laser in mW.

        Args:
            power_mw (int): The power in mW to set.
        """
        return self.send_command(f"POWER={power_mw}")

    def get_power(self):
        """Returns the power of the laser read from the internal photodiode."""
        return self.send_command("POWER?")

    def set_startup_power(self, power_mw):
        """
        Sets the default start-up power in mW.

        Args:
            power_mw (int): The start-up power in mW.
        """
        return self.send_command(f"STPOW={power_mw}")

    def recalibrate_APC(self, power_mw):
        """
        Recalibrates the APC mode with the specified power in mW.

        Args:
            power_mw (int): The power in mW for recalibration.
        """
        return self.send_command(f"ACTP={power_mw}")

    def write(self):
        """Stores APC calibration, STEN, and STPOW in memory."""
        return self.send_command("WRITE")

    def get_laser_temp(self):
        """Returns the temperature of the laser head in degrees centigrade."""
        return self.send_command("LASTEMP?")

    def get_psu_temp(self):
        """Returns the temperature of the PSU in degrees centigrade."""
        return self.send_command("PSUTEMP?")
    
    def get_status(self):
        """Returns the status of the Interlock."""
        return self.send_command("STATUS?")
    
    def get_timers(self):
        """
        Returns the timers of the laser and PSU, including:
        - Total time the system has been powered
        - Total time the diodes have been powered
        - Total time the diodes have been powered >1 A
        """
        return self.send_command("TIMERS?")

    def get_version(self):
        """Returns the PSU version information."""
        return self.send_command("VERSION?")
