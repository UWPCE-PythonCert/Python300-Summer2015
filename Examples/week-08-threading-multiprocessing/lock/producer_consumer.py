import threading
import time
import random
import Queue

def producer(q,aint):
    #time.sleep(random.random())
    print "Producer.put: %s" % aint
    q.put( aint )

def consumer(q):
    while not q.empty():
        value = q.get()
        print "Consumer.get: %s" % value

if __name__ == '__main__':

    q = Queue.Queue()
    for n in range(1,11):
        # create producer threads, they do one thing well
        threading.Thread(target=producer, args=(q,n)).start()
    consumer = threading.Thread(target=consumer, args=(q,)).start()

# toggle time, change consumer loc, poison pill


