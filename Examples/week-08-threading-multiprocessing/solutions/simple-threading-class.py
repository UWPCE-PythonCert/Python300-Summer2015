import sys
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)
import threading
import time
# output order, log format, name, need to join, sys.exit, raise Exception

class BusyWork( threading.Thread ):

    def run(self):
        for i in xrange(3):
            logging.debug("hello from thread %s" % threading.current_thread().name)
            time.sleep(2)

threads = []
for i in xrange(3):
    thread = BusyWork()
    thread.start()
    threads.append(thread)

for thread in threads:
    logging.debug( "join()" )
    thread.join()


