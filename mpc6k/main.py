from serial.tools import list_ports
import click
import re
from math import isnan
from simple_server.server import SocketServer
import signal



server: SocketServer = None


def val_from_dict(key: str, dict: dict):
    return dict[key] if key in dict else None


def float_or_nan(val: str):
    try:
        return float(val)
    except TypeError:
        return float("nan")


def __connect(port: str or None) -> Controller:
    """
    Connect to the MCM3000 controller.
    Connect to the MCM3000 controller and return a Controller object.

    Parameters
    ----------
    port : int or None (default=None) The serial port to connect to. If None, a list of available ports will be printed and the user will be prompted to select one.
    """
    if not port:
        # Get a list of available serial ports and prompt the user to select one
        ports = sorted(list(list_ports.comports()))
        if not ports:
            # No serial ports found so return None
            click.echo("No serial ports found.")
            return None
        elif len(ports) == 1:
            # Only one serial port found so use it
            port = ports[0].device
            click.echo(f"Using serial port {port}.")
        else:
            # Multiple serial ports found so prompt the user to select one
            click.echo("Multiple serial ports found select one by its index:")
            for i, p in enumerate(ports):
                click.echo(f"{i}. {p.device} ({p.description})")
            port = ports[click.prompt("Select a serial port", type=int)].device
    if not port:
        # No serial port selected so return None
        click.echo("No serial port selected.")
        return None
    # TODO: Return a Controller object





def signal_handler(_, __):
    """
    Ensure the server is stopped when the program is terminated.
    """
    print("Program terminated. Stopping server...")
    if server:
        server.stop_with_err("Program terminated.")
    quit(1)


def generate_help():
    """
    Generate the help message.
    """
    #TODO: Update this help message to reflect the PSU commands
    return """
Commands:
connect - Connect to the stage controller
zero - Zero the stage
    <direction> [distance][ ][unit] - Move the stage the specified distance in the specified direction. If distance is not specified, defaults to 1. If unit is not specified, defaults to um.
exit - Exit the program
help - Print this help message
"""



def process_cmd(cmd: str, port: str = None, **kwargs) -> str:
    """
    Process a command.

    Parameters
    ----------
    cmd : str
        The command to process
    [port] : str
        The serial port to use

    Returns
    -------
    str
        The response to the command
    """
    #TODO: Update this function to process the PSU commands
    server = kwargs["server"] if "server" in kwargs else None
    global ctrl
    msg = ""
    if cmd == "exit":
        hard_stop()
    elif cmd == "connect":
        ctrl = __connect(port)
        if not ctrl:
            server.stop_with_err("Failed to connect to stage controller.")
            click.echo("Failed to connect to stage controller.")
            quit(1)
    elif cmd == "zero":
        # zero command detected so zero the stage
        try:
            __set_zero(ctrl)
        except Exception as e:
            msg = f"Failed to zero stage: {e}"
    elif cmd == "help":
        # help command detected so print help
        msg = generate_help()
    elif cmd.startswith("goto"):
        goto(cmd, ctrl)
    elif cmd == "pos":
        msg = f"{ctrl.position_um[Y]} {ctrl.position_um[X]}"
    else:
        # Move command detected so handle it
        try:
            msg = __handle_move(cmd, ctrl)
        except Exception as e:
            msg = f"Failed to move stage: {e}"
    if server:
        server.send(f'{cmd} {msg}')
    print(msg)


@click.command()
@click.option("--port", "-p", type=str, help="Serial port name")
def main(port):
    global server
    """A simple CLI for controlling the Thorlabs MCM3000 stage controller."""
    def start_server(cmd, server):
        try:
            process_cmd(cmd, server=server)
        except Exception as e:
            print(e)
    signal.signal(signal.SIGINT | signal.SIGTERM, signal_handler)
    server = SocketServer()
    server.start(lambda cmd, server=server: 
                 start_server(cmd, server) # server is only populated in the callback from the server
                 )
    while True:
        cmd = click.prompt("Enter a command", type=str).lower().strip()
        process_cmd(cmd, port)


if __name__ == "__main__":
    main()
