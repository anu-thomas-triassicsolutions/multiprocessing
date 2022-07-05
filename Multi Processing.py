import time
import logging
import multiprocessing
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# initialization
event_handler = LoggingEventHandler()
observer = Observer()

folder1 = r"C:\Users\Anu\Triassic solutions\watching program\folder1"
folder2 = r"C:\Users\Anu\Triassic solutions\watching program\folder2"


def monitor_folder(folder):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)s', datefmt='%Y-%m-%d %H:%H:%S')
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)  # set sleep time
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    m = multiprocessing.Process(target=monitor_folder, args=(folder1,))
    m1 = multiprocessing.Process(target=monitor_folder, args=(folder2,))
    m.start()
    m1.start()
