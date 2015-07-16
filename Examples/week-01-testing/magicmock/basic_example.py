from mock import MagicMock

class Foo(object):

    def foo(self,*args):
        print "[ FOO ]"

    def bar(self):
        print "[ BAR ]"

#  mock up Foo class methods
Foo = MagicMock(Foo)
foo = Foo()
#assert foo.bar() == "foo return"

#
#  MagicMock just returns a mock object
#  that we can play with by adding
#  arbitrary methods and attributes
#
#
foo.foo.return_value = "foo return"
assert foo.foo() == "foo return"
print foo.foo.call_count
assert foo.foo.call_count == 1
print foo.foo()
print foo.foo.call_count
assert foo.foo.call_count == 2
assert foo.foo.called == True
foo.foo('blah')
# NOTE: mocked objects have a few assertion methods on them
foo.foo.assert_called_with('blah')
foo.foo.assert_called_any('blah')

#
# raise an exception by assigning to the side_effect attribute
#
class CustomException( Exception ):
    def __init__(self):
        super(CustomException, self).__init__("error: custom foobar")
foo.foo.side_effect = CustomException

try:
    foo.foo()
except CustomException:
    print "caught it"
    assert 1 == 1 # we got here, so that means something
