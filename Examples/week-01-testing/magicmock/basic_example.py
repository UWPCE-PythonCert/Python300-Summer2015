from mock import MagicMock

class Foo(object):

    def foo(self):
        print "[ FOO ]"

    def bar(self):
        print "[ BAR ]"

#  mock up Foo class methods
Foo.bar = MagicMock(return_value="foo return")
foo = Foo()
assert foo.bar() == "foo return"

#
#  MagicMock just returns a mock object
#  that we can play with by adding
#  arbitrary methods and attributes
#
mock_object = MagicMock()
mock_object.foo.return_value = "foo return"
assert mock_object.foo() == "foo return"
print mock_object.foo.call_count
assert mock_object.foo.call_count == 1
print mock_object.foo()
print mock_object.foo.call_count
assert mock_object.foo.call_count == 2
assert mock_object.foo.called == True
mock_object.foo('blah')
# NOTE: mocked objects have a few assertion methods on them
mock_object.foo.assert_called_with('blah')

#
# raise an exception by assigning to the side_effect attribute
#
class CustomException( Exception ):
    def __init__(self):
        super(CustomException, self).__init__("error: custom foobar")
mock_object.foo.side_effect = CustomException

try:
    mock_object.foo()
except CustomException:
    print "caught it"
    assert 1 == 1 # we got here, so that means something
