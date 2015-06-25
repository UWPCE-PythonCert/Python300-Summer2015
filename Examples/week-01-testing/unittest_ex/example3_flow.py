import unittest

def setUpModule():
    print "setUpModule"

def tearDownModule():
    print "tearDownModule"

class TestTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "setUpClass"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"

    def setUp(self):
        print "setUp"

    def tearDown(self):
        print "tearDown"

    def test_add(self):
        print "test_add"
        self.assertEqual(2+2, 4)

    def test_len(self):
        print "test_len"
        self.assertEqual(len('foo'), 3)

    @unittest.skip("not implemented, but needs to be")
    def test_foo(self):
        print "test_foo"

if __name__ == '__main__':
    unittest.main()

# NOTE: order, class needed for a test

