import mock

mock_object = mock.MagicMock()
mock_object.foo.return_value = "foo return"
assert mock_object.foo() == "foo return"
print mock_object.foo.call_count
assert mock_object.foo.call_count == 1
print mock_object.foo()
print mock_object.foo.call_count
assert mock_object.foo.call_count == 2

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
