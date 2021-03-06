#!/usr/bin/env python

import threading
import time

x = 0
def func():
    global x
    x += 1

threads = []
#
# with enough threads 
# there's sufficient overhead 
# to cause a race condition
#
for i in xrange(1000):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print x
