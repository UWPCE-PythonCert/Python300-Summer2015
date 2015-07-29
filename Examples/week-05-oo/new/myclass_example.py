class MyClass(object):
    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        print "creating new class %s" % cls
        instance = super( MyClass, cls ).__new__( cls, *args, **kwargs )
        instance.foo = "blah"
        return instance

