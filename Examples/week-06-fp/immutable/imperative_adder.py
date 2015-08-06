#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
import logging
console = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console)

class Adder(object):

    def __init__(self,start):
        self.n = start

    def add(self,m):
        self.n += m

if __name__ == '__main__':

    thread_pool = ThreadPool(processes=1000)
    adder = Adder(0)
    instances = [adder] * 5000

    def execute(adder_instance):
        adder_instance.add(1)
    thread_pool.map(execute,instances)

    logger.debug("[ FINAL COUNT ]: {}".format(adder.n))