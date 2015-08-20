import threading
import time

lock = threading.Lock()

def f():
    if not lock.acquire(False):
        print "%s couldn't get lock" % threading.current_thread().name
        # retry logic?
    else:
        print "%s got lock" % threading.current_thread().name
        time.sleep(1)
        lock.release()

threading.Thread(target=f).start()
threading.Thread(target=f).start()
threading.Thread(target=f).start()
