from events import OutputEvent, SetmodeEvent
import socket
import json

LOW = 0
HIGH = 1

BOARD = 10
BCM = 11


def setmode(mode):
    setmode_event = SetmodeEvent(mode)
    _send_event(setmode_event.as_dict())


def setup():
    pass


def input(channel):
    pass


def output(channel, outmode):
    output_event = OutputEvent(channel, outmode)
    _send_event(output_event.as_dict())


def cleanup(channel=None):
    pass


def _send_event(event):
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = '/tmp/uln2003'
    try:
        sock.connect(server_address)

        message = str.encode(json.dumps(event))
        sock.sendall(message)
    except socket.error as msg:
        print('Could not connect to socket %s' % msg)


if __name__ == "__main__":
    output(2, 1)
