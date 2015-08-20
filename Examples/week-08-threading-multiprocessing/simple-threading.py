import sys
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)
import threading
import time
# output order, log format, name, join?, need to join, sys.exit, raise Exception

def func():
    for i in xrange(3):
        # simulate work
        logging.debug("hello from thread %s" % threading.current_thread().name)
        time.sleep(2)

if __name__ == '__main__':

    threads = []
    for i in xrange(3):
        thread = threading.Thread(target=func, args=())
        thread.start() # calls Thread.run()
        threads.append(thread)

    for thread in threads:
        logging.debug( "join()" )
        thread.join()

    logging.debug("after joining")

