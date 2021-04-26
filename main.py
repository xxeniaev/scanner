import sys
import socket
import time
from datetime import datetime
import threading
from queue import Queue
import settings
from scanner import Scanner

# что с 21 портом
# udp порты тоже


def consumer(q):
    while True:
        s = q.get()
        try:
            s.scan_tcp()
            # s.scan_udp()
        finally:
            q.task_done()


if __name__ == '__main__':
    # Defining a target
    # translate hostname to IPv4
    try:
        target = socket.gethostbyname(sys.argv[1])
    except IndexError:
        print("\n Set arguments")
        sys.exit()

    # Add Banner
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    seconds = int(round(time.time()))

    # producer/consumer pattern
    queue = Queue()
    # will scan ports between 1 to 65 535
    for item in range(1, 65535):
        queue.put(Scanner(target, item))

    try:
        # turn on the consumer thread
        consumers = [threading.Thread(
            target=consumer, args=(queue,), daemon=True) for _ in range(settings.THREADS)]
        for consumer_item in consumers:
            consumer_item.start()
    except KeyboardInterrupt:
        print("Exit")
        sys.exit()
    except socket.gaierror:
        print("Hostname Could Not Be Resolved")
        sys.exit()
    except socket.error:
        print("Server not responding")
        sys.exit()

    queue.join()

    print("-" * 50)
    print('All work completed', round(time.time()) - seconds, "sec")
