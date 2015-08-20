import sys
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)
import threading
import time

def func():
    for i in xrange(3):
        logging.debug("hello from thread %s" % threading.current_thread().name)
        time.sleep(2)


if __name__ == '__main__':
    threads = []
    for i in xrange(3):
        thread = threading.Thread(target=func, args=())
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # toggle me, pids
    for thread in threads: thread.join()


