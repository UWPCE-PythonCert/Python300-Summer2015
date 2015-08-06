#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from Queue import Queue
import logging
console = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console)

def add(n,m):
    return n+m

if __name__ == '__main__':

    thread_pool = ThreadPool(processes=1000)
    queue = Queue()
    queue.put(0)
    items = [queue] * 5000

    def execute(queue):
        queue.put(add(queue.get(),1))

    thread_pool.map(execute,items)

    logger.debug("[ FINAL COUNT ]: {}".format(queue.get()))