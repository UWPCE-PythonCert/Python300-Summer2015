import unittest

def bad_funk():
    return [][0]

class TestTest(unittest.TestCase):

    def test_asserts(self):
        self.assertEqual(len('foo'), 3)
        self.assertNotEqual(1, 3)
        self.assertTrue(len('foo')==3)
        self.assertFalse(1==3)
        self.assertIn(1,[1,2,3])
        self.assertRaises(IndexError,bad_funk)

if __name__ == '__main__':
    unittest.main()

# NOTE: msg

