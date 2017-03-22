# -*- coding: utf-8 -*-
import socket
from pymouse import PyMouse


UDP_IP = '192.168.1.121'
UDP_PORT = 5000
MAX_BUFFER = 1024


class Mouse(object):
    def __init__(self, coordinates):
        if not isinstance(coordinates, tuple):
            raise ValueError("Coordinates expected %s, got: %s", (type(tuple), type(coordinates)))
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        if not isinstance(coordinates, tuple):
            raise ValueError

        if self.coordinates[0] == coordinates[0] and self.coordinates[1] == coordinates[1]:
            return

        self.coordinates = coordinates


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    py_mouse = PyMouse()
    mouse = Mouse(py_mouse.position())

    while True:
        mouse.set_coordinates(py_mouse.position())
        coordinates = mouse.get_coordinates()
        s.sendto("%s %s" % (coordinates[0], coordinates[1]), (UDP_IP, UDP_PORT))
