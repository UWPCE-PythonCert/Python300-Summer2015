import threading
import time
lock = threading.Lock()

def f():
    # toggle
    #lock.acquire()
    print "%s got lock" % threading.current_thread().name
    time.sleep(1)
    print "Done sleeping"
    #lock.release()

for n in range(25):
    threading.Thread(target=f).start()


