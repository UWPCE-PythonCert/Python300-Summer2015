import inspect, sys

def a(x):
    x = 'a_bloop'
    print "BEFORE: %s" % x
    b()
    print "AFTER: %s" % x

def b():
    frame = sys._getframe(1)
    frame.f_locals[ 'x' ] = 'BAM'
    #assert globals() == frame.f_locals

a('blah')
