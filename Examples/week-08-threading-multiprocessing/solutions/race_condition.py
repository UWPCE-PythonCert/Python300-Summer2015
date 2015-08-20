#!/usr/bin/env python
import threading
import time
lock = threading.Lock()

x = 0
def func():
    global x
    # NOTE: cm form
    lock.acquire()
    y = x # read
    y += 1 # update
    x = y # write
    lock.release()

#
# with enough threads 
# there's sufficient overhead 
# to cause a race condition
#
threads = []
for i in xrange(1000):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print x
