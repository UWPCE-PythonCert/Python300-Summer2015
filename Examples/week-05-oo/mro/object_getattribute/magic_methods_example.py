class Foo(object):

    age = 20

    def __init__(self):
        self.name = "name"

    @property
    def height(self):
        return 6.4

    def __getattr__(self,name):
        print "__getattr__ called for %s" % name

    def __getattribute__(self, name):
        print "__getattribute__ called for %s" % name
        return super(Foo,self).__getattribute__(name)


if __name__ == '__main__':
    foo = Foo()
    print foo.age
    print foo.name
    print foo.height
    foo.barf



