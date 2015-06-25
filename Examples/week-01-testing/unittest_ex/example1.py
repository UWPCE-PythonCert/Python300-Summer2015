import unittest

class TestTest(unittest.TestCase):

    def setUp(self):
        print "setUp"

    def test_add(self):
        print "test_add"
        self.assertEqual(2+2, 4)

    def test_len(self):
        print "test_len"
        self.assertEqual(len('foo'), 3)

    @unittest.skip("not implemented, but needs to be")
    def test_foo(self):
        print "test_foo"
        pass

if __name__ == '__main__':
    unittest.main()

# NOTE: call, order, asserts

