import socket
import time
from enum import Enum

close_connection = False # Set to True to close the connection

class SSClient:
    class Status(Enum):
        Disconnected = 0
        Connected = 1
        Receiving = 2
        Transmitting = 3
        Disconnecting = 4
        Connecting = 5
        Disconnect = 6 # This is a custom status for the recv_loop to use to close the connection.
    def __init__(self) -> None:
        self.__socket = None
        self.__status = self.Status.Disconnected

    def set_status(self, status: Status) -> None:
        """
        Set the status of the client.
        
        parameters
        ----------
        status : Status The status of the client.
        """
        self.__status = status

    def get_status(self) -> Status:
        """
        Get the status of the client.

        Returns
        -------
        Status The status of the client.
        """
        return self.__status
    
    def connect(self, host: str, port: int) -> None:
        """
        Connect to a socket server.
        
        parameters
        ----------
        host : str The host to connect to.
        port : int The port to connect to.
        """
        self.set_status(self.Status.Connecting)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__socket.connect((host, port))
        except ConnectionRefusedError:
            self.__socket = None
            self.set_status(self.Status.Disconnected)
        finally:
            self.set_status(self.Status.Connected) if self.__socket else self.set_status(self.Status.Disconnected)
    
    def disconnect(self) -> None:
        """
        Disconnect from the socket server.
        """
        self.set_status(self.Status.Disconnecting)
        try:
            self.__socket.shutdown(socket.SHUT_WR)  # Step 1: Client-side shutdown
            self.__socket.close()  # Step 3: Closing the socket
        except AttributeError:
            pass
        finally:
            self.set_status(self.Status.Disconnected)
            self.__socket.close()
        self.__socket = None

    
    def send(self, message: str) -> None:
        """
        Send a message to the socket server.
        
        parameters
        ----------
        message : str The message to send to the socket server.
        """
        self.set_status(self.Status.Transmitting)
        self.__socket.sendall(message.encode("utf-8"))
        self.set_status(self.Status.Connected)
        
    def recv(self) -> str:
        """
        Receive a message from the socket server.
        
        returns
        -------
        str The message received from the socket server.
        """
        self.set_status(self.Status.Receiving)
        recvd = self.__socket.recv(1024).decode("utf-8")
        self.set_status(self.Status.Connected)
        return recvd
    



if __name__ == "__main__":
    client = SSClient()
    client.connect("localhost", 5000)
    client.send('pos\n')
    time.sleep(3)
    client.send('exit\n')
    time.sleep(3)