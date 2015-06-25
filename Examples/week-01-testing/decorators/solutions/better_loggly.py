import functools

def loggly(muffle=False):

    def loggly_decorator(func):
        def logger(*args, **kwargs):
            if not muffle:
                print "executing '{}'".format( func.__name__ )
                print "\twith args: {}".format( args )
                print "\twith kwargs: {}".format( kwargs )
            return func(*args, **kwargs)
        return logger

    return loggly_decorator


def test1(x,y):
    return x + y
test1 = loggly(muffle=False)( test1 )

@loggly( muffle=False )
def test2(x,y):
    return x * y 

if __name__ == '__main__':
    test1(10,10)
    test2(10,10)
    
