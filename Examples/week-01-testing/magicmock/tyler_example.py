from mock import MagicMock

class Foo(object):

    def __init__(self, bar_instance):
        self.bar = bar_instance

    def run(self,*args):
        name = bar.name

        if name is not None:
            print "name is not None"

        return bar.barf()

class Bar(object):
    name = "barry white"

    def barf(self):
        return "barfed"


if __name__ == '__main__':
    bar = Bar()
    foo = Foo(bar)
    print foo.run()
