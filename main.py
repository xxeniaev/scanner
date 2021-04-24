import sys
import socket
import time
from datetime import datetime
import multiprocessing.dummy as mp


def scan(port):
    # will scan ports between 1 to 65 535
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # returns an error indicator
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))

    if port % 10 == 0:
        print(port)

    s.close()


if __name__ == '__main__':
    # Defining a target
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])

    # Add Banner
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    seconds = int(round(time.time()))

    try:
        p = mp.Pool(4)
        p.map(scan, range(1, 50))  # range(0,1000) if you want to replicate your example
        p.close()
        p.join()

    except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()

    print("-" * 50)
    print('All work completed', round(time.time()) - seconds, "sec")
