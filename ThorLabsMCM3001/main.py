from ThorLabsMCM3001.thorlabs_MCM3000 import Controller
from serial.tools import list_ports
import click
import re
from math import isnan
from simple_server.server import SocketServer
import signal

# Constants
STAGE = "PLS-XY"
X, Y, Z = 0, 1, 2


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
    else:
        # Serial port selected so use it
        click.echo(f"Using serial port {port}.")
    try:
        ctrl = Controller(port, stages=(STAGE, STAGE, None),
                          reverse=(False, False, False))
        click.echo(f"Connected to MCM3000 on serial port {port}.")
    except Exception as e:
        click.echo(f"Failed to connect to serial port {port}.")
        click.echo(e)
        return None
    return ctrl


def __handle_move(cmd: str, ctrl: Controller) -> str:
    """
    Handle a move command.
    Move command syntax: <direction> [distance][ ][unit]
    <direction> is one of left, right, forward, backward, up, down
    [distance] is an optional distance to move. If not specified, defaults to 1.
    [unit] is an optional unit. If not specified, defaults to um.

    Parameters
    ----------
    cmd : str
        The move command
    ctrl : Controller
        The controller to use

    Notes
    -----
    The space between the distance and unit is optional.

    Raises
    ------
    ValueError if the command is invalid.
    """

    # Regular expression for parsing commands
    # matches: <command> [distance][ ][um|mm] where [] denotes optional. Space between distance and unit is optional.
    # if distance is not specified, it defaults to 1. If unit is not specified, it defaults to um.
    expr = r"(?P<dir>left|right|up|down|in|out)(?:\s(?P<pos>abs|rel))?(?:\s(?P<dist>-?\d+\.?\d*|\.\d+))?(?:\s?(?P<unit>[um]m))?"
    parsed = re.match(expr, cmd)
    if not parsed:
        raise ValueError(f"Invalid command: {cmd}")
    parts = parsed.groupdict()
    direction = val_from_dict("dir", parts).strip()
    distance = float_or_nan(val_from_dict("dist", parts))
    unit = val_from_dict("unit", parts) or "um"
    # if pos is not abs, then it is rel
    relative = val_from_dict("pos", parts) != "abs"

    # if distance is not supplied default to 0.001 mm
    if isnan(distance):
        distance = 0.005
        unit = "mm"

    # Check if the distance is valid
    #assert(distance >= 0)

    # Convert the distance to um if necessary
    if unit == "mm":
        distance *= 1000

    # Move the stage
    directions = {
        "left": (Y, distance),
        "right": (Y, -distance),
        "up": (X, -distance),
        "down": (X, distance),
    }

    if direction in directions:
        axis, move_distance = directions[direction]
        ctrl.move_um(axis, move_distance, relative=relative)
        return f"Moved stage {direction} by {distance} um." if relative else f"Moved stage {direction} to {distance} um."
    elif direction in ["up", "down"]:
        return "Not implemented yet."
    else:
        raise ValueError(f"Invalid command: {cmd}")  # Should never happen


def __set_zero(ctrl: Controller):
    """
    Zero the stage.
    TODO: Make this work for client-server mode.
    """
    # Check if the stage is at the zero position
    if click.prompt("Is the stage at the zero position?", type=bool):
        # set the zero position
        ctrl._set_encoder_counts_to_zero(X)
        ctrl._set_encoder_counts_to_zero(Y)
        click.echo("Stage zeroed.")
    else:
        click.echo(
            "Please manually move the stage to the zero position and try again.")


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
    return """
Commands:
connect - Connect to the stage controller
zero - Zero the stage
    <direction> [distance][ ][unit] - Move the stage the specified distance in the specified direction. If distance is not specified, defaults to 1. If unit is not specified, defaults to um.
exit - Exit the program
help - Print this help message
"""


def __auto_complete(partial_cmd: str):
    '''Auto complete commands'''
    pass  # TODO


def goto(cmd: str, ctrl: Controller):
    '''
        Go to a position

        Parameters
        ----------
        cmd : str
            The goto command
        ctrl : Controller
            The controller to use
    '''
    x, y = cmd.split(" ")[1:]
    new_cmd = f"left abs {x}\n"
    __handle_move(new_cmd, ctrl)
    new_cmd = f"down abs {y}\n"
    __handle_move(new_cmd, ctrl)

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

    server = kwargs["server"] if "server" in kwargs else None
    global ctrl
    msg = ""
    if cmd == "exit":
        if server:
            server.stop()

        quit(0)
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
    """A simple CLI for controlling the Thorlabs MCM3000 stage controller."""
    def start_server(cmd, server):
        try:
            process_cmd(cmd, server=server)
        except Exception as e:
            print(e)
    signal.signal(signal.SIGINT | signal.SIGTERM, signal_handler)
    server = SocketServer()
    server.start(lambda cmd, server=server: 
                 start_server(cmd, server)
                 )
    while True:
        cmd = click.prompt("Enter a command", type=str).lower().strip()
        process_cmd(cmd, port)


if __name__ == "__main__":
    main()