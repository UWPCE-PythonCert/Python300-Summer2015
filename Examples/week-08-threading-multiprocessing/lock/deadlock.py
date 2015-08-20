import threading, time

a_lock = threading.Lock()
b_lock = threading.Lock()

def calc():
    print "%s acquiring lock a_lock" % threading.currentThread().name
    a_lock.acquire()
    time.sleep(5)

    print "%s acquiring lock b_lock" % threading.currentThread().name
    b_lock.acquire()
    time.sleep(5)

    a_lock.release()
    b_lock.release()


def calc2():
    print "%s acquiring lock b_lock" % threading.currentThread().name
    b_lock.acquire()
    time.sleep(5)

    print "%s acquiring lock a_lock" % threading.currentThread().name
    a_lock.acquire()
    time.sleep(5)

    b_lock.release()
    a_lock.release()

threads = []
t = threading.Thread(target=calc)
t.daemon = True
t.start()
threads.append(t)

t = threading.Thread(target=calc2)
t.daemon = True
t.start()
threads.append(t)

for t in threads: t.join()

