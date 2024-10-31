import socket
import threading
from enum import Enum
from contextlib import closing
from typing import Callable




class enum_status(Enum):
    started = 0
    stopping = 1
    stopped = 2

def _val_from_key(key: str, dict: dict) -> bool:
    """
    Return the value of a key in a dictionary if the key exists, otherwise return None.
    Return the value of a key in a dictionary if the key exists, otherwise return None.

    Parameters
    ----------
    key : str The key to look for in the dictionary.
    dict : dict The dictionary to look for the key in.
    """
    return dict[key] if key in dict else None

class SocketServer(object):
    __doc__ = 'Socket server for the ThorLabs MCM3000 controller.\n    Socket server for the ThorLabs MCM3000 controller.\n    '
    def __init__(self, **kwargs) -> None:
        self.port = _val_from_key("port", kwargs) or 5000
        self.host = _val_from_key("host", kwargs) or "0.0.0.0"
        self.buffer_size = _val_from_key("buffer_size", kwargs) or 1024
        self.__thread = None
        self.__status = enum_status.stopped
        self.__connection = None
        
    def stop_with_err(self, message: str) -> None:
        """
        Send an error message to the client and stop the server.
        parameters: message : str The error message to send to the client.
        """
        
        if self.__connection:
            self.__connection.sendall(f"ERROR: {message}\n".encode("utf-8"))
        
        self.stop()
        
    def status(self) -> enum_status:
        """
        returns
        -------
        enum_status The status of the socket server.
        """
        return self.__status
    
    def thread(self) -> threading.Thread:
        """
        returns
        -------
        threading.Thread The thread the socket server is running on.
        """
        return self.__thread
        
    def start(self, on_recv: Callable[[str], None]) -> threading.Thread:
        """
        Start the socket server.
        
        Start the socket server on a new thread and return the thread.
        
        parameters
        ----------
        on_recv : Callable[[str], None] The function to call when a message is received.
        
        returns
        -------
        threading.Thread The thread the socket server is running on.
        """
        thread = threading.Thread(target=self.__start, args=(on_recv,))
        thread.start()
        self.__thread = thread
        return thread
    
    def stop(self) -> None:
        """
        Signal the socket server to stop.
        
        Blocks until the socket server has stopped.
        """
        self.__status = enum_status.stopping
        self.__server_socket.close()  # Close the server socket to unblock the s.accept() call
        self.__thread.join()
        
    def send(self, message: str) -> None:
        """
        Send a message to the client.
        
        parameters
        ----------
        message : str The message to send to the client.
        """
        if self.__connection:
            self.__connection.sendall(f"{message}\n".encode("utf-8")) # Send the message to the client
    
    def __start(self, on_recv: Callable[[str], None]) -> None:
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with closing(self.__server_socket) as s:
            s.settimeout(1.0)  # Set timeout to 1 second for example
            server_address = (self.host, self.port)
            s.bind(server_address)
            s.listen(1)

            data = ""
            while self.__status != enum_status.stopping:
                self.__connection = None
                try:
                    connection, _ = s.accept()
                    self.__connection = connection
                    with closing(connection):
                        while True:
                            chunk = connection.recv(self.buffer_size)
                            if chunk:
                                data += chunk.decode("utf-8")
                                if "\n" in data:
                                    # Split by newline, keep the remainder in the buffer
                                    *lines, data = data.split("\n")
                                    for line in lines:
                                        resp = on_recv(line)
                                        if resp:
                                            connection.sendall(resp.encode("utf-8"))
                            else:
                                # No more data -- break the loop
                                break
                except socket.timeout:
                    pass  # No connection within timeout, check status and keep looping if not stopping
                except ConnectionResetError:
                    # Handle the case where the connection was reset during shutdown
                    break

            self.__status = enum_status.stopped
            self.__thread = None
            self.__connection.close()