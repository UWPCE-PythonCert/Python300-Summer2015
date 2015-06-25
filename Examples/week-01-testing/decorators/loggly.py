
def loggly(func):
    def logger(*args, **kwargs):
        if not kwargs.get( 'muffle', False ):
            print "executing '{}'".format( func.__name__ )
            print "\twith args: {}".format( args )
            print "\twith kwargs: {}".format( kwargs )
        return func(*args, **kwargs)
    return logger


def test1(x,y):
    return x + y
test1 = loggly( test1 )

@loggly
def test2(x,y,muffle=True):
    return x * y 

if __name__ == '__main__':
    test1(10,10,muffle=True)
    test2(10,10)
    
