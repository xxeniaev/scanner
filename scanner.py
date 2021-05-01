import os
import socket


class Scanner:
    def __init__(self, target, port):
        self.port = port
        self.target = target

    def scan_tcp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((self.target, self.port))
        if result == 0 and self.port != 21:
            print("Port {} is open {}".format(self.port, 'TCP'))

        s.close()

    def scan_udp(self):
        # показывает все порты открытыми
        # """ send to /dev/null 2>&1 to suppress terminal output """
        # res = os.system("nc -vnzu " + str(self.target) + " " + str(self.port) + " > /dev/null 2>&1")
        # if res == 0:
        #     print("Port {} is open {}".format(self.port, 'UDP'))

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.bind((self.target, self.port))
            print("Port {} is open {}".format(self.port, 'UDP'))
        except OSError:
            pass
