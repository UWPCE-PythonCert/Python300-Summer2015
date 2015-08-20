import string
import threading
import Queue
import math

def producer(q, chunked_list):
    for alpha in chunked_list:
        try:
            q.put( ord(alpha) )
        except TypeError:
            q.put( None )

def consumer(q):
    while True:
        value = q.get()
        if value is None:
            break
        print value

if __name__ == '__main__':

    num_threads = 5
    alphas = list( string.ascii_lowercase + string.ascii_uppercase )
    chunk_size = int( math.ceil( len(alphas) / float(num_threads) ) )
    print chunk_size

    q = Queue.Queue()
    threading.Thread(target=consumer, args=(q,)).start()
    for i in range(num_threads):
        start = chunk_size*i
        end = chunk_size*(i+1)
        print start,end
        alpha_slice = alphas[start:end]
        print alpha_slice
        threading.Thread(target=producer, args=(q,alpha_slice)).start()

    # poison pill
    threading.Thread(target=producer, args=(q,[None])).start()
        


