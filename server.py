import socket
from pymouse import PyMouse


UDP_IP = '0.0.0.0'
UDP_PORT = 5000
MAX_BUFFER = 1024


class Mouse(object):

    def __init__(self):
        self.py_mouse = PyMouse()
        self.coordinates = None
        self.width = self.py_mouse.screen_size()[0]
        self.height = self.py_mouse.screen_size()[1]
        self.mouse_width = None
        self.mouse_height = None

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        if not isinstance(coordinates, tuple):
            raise ValueError

        if self.coordinates[0] == coordinates[0] and self.coordinates[1] == coordinates[1]:
            return
        self.coordinates = coordinates

    def set_mouse_coordinates(self):
        self.mouse_width = self.width * self.coordinates[0]
        self.mouse_height = self.height * self.coordinates[1]

    def set_mouse_position(self):
        self.py_mouse.move(self.mouse_width, self.mouse_height)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((UDP_IP, UDP_PORT))
    mouse = Mouse()

    while True:
        data, addr = s.recvfrom(MAX_BUFFER)
        data_list = data.split(" ")
        mouse.set_coordinates(tuple(data_list))
        print mouse.get_coordinates()
