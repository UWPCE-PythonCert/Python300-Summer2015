import cPickle as pickle

class Foo(object):

    def __new__(cls, *args, **kwargs):
        print "__new__ called"
        return super( Foo, cls ).__new__( cls, *args, **kwargs )

    def __init__(self):
        print "__init__ called"

foo = Foo()
print foo

foo_pickle = pickle.dumps(foo)
print foo_pickle

new_foo = pickle.loads(foo_pickle)
print new_foo

