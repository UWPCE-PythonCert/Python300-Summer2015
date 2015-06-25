import time

def timed_func(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "Function '{}' took {} seconds to run".format( func, elapsed )
        return result
    return timed

@timed_func
def test():
    print "Testing..."
    time.sleep( 10 ) # seconds
    print "and...done"

if __name__ == '__main__':
    test()

    
