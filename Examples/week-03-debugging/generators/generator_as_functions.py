import time
"""
this module is an illustrative example
of how to think about building a generator
using straight function callbacks:
the term for this type of pattern is
a continuation using callcc ( call with current continuation )
if you want to look that up
"""
def next(val):
    print "next.."
    def fake_yield(callback):
        time.sleep(1)
        callback(val)
        print "continue..." 

    return fake_yield

def continuation_manager(wrapper):
    val = []
    def callback(*args, **kwargs):
        val[:] = [args, kwargs]
        print "updated scoped value = {}".format(val)

    wrapper(callback)
    return val

if __name__ == '__main__':
    #
    # NOTE: order of execution
    # NOTE: return value
    #
    print "executing..."
    for i in range(5):

        def wrapper( continuation_func ):
            next(i)( continuation_func )

        continuation_manager( wrapper )


