class ParentFoo(object):
    def bound_method(self):
        print "ParentFoo bound_method"

    @classmethod
    def unbound_method(cls):
        print "ParentFoo unbound_method"

class FooChild(ParentFoo):

    def bound_method(self):
        print "FooChild bound_method"

    @staticmethod
    def unbound_method():
        print "FooChild unbound_method"

if __name__ == '__main__':
    foo = FooChild()

    print foo.bound_method
    foo.bound_method() # method is bound to the foo instance
    super(type(foo),foo).bound_method()

    print FooChild.unbound_method
    FooChild.unbound_method() # method is not bound
    super(FooChild,FooChild).unbound_method()

'''
NOTE:
1. review staticmethod versus classmethod
'''