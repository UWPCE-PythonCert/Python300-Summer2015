class Foo(object):

    def __init__(self, bar=None):
        self.bar = bar or 'default bar'

    def show(self):
        return 'show() called on {} with self.bar = {}'.format(self,self.bar)
        

if __name__ == '__main__':
    
    foobar = Foo('bad news bears')

    print Foo.__dict__[ 'show' ]
    print Foo.__dict__[ 'show' ](foobar) # what, why?
    print Foo.show
    try:
        print Foo.show()
    except TypeError, e:
        print e
        print Foo.show(foobar) # what, why?

    print foobar.show
    print foobar.show()

    def show_override(self): print "haha!"
    foo1 = Foo('foo1')
    print foo1.show()
    foo2 = Foo('foo2')
    print foo2.show()
    Foo.show = show_override
    print foo1.show() # what, why?
    print foo2.show() # what, why?

    





