from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)

    print pool.apply(f, (10,))

    """
    result = pool.apply_async(f, (10,))
    print result.get()
    """

    #print pool.map(f, range(10))

    """
    result = pool.map_async(f, range(10))
    print result.get()
    """

    """
    it = pool.imap(f, range(10))
    for i in it:
        print i
    """

    """
    # add sleep to f()
    result = pool.map_async(f, range(10))
    print result.get(timeout=1)
    """
    

    

    

