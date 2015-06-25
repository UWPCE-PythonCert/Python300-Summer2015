import string
import unittest

class AsciiCounter( object ):
    """
    returns dict of total number of ascii character occurences
    """

    def new_or_add( self, ascii_char_key, char_dict ):
        num_occurences = char_dict.get( ascii_char_key, None )
        if num_occurences is None:
            # new
            char_dict[ ascii_char_key ] = 1
            return 
        # increment
        char_dict[ ascii_char_key ] = num_occurences + 1
        return
            
    def count_all( self, ascii_str ):
        results = {}
        for ascii_char in ascii_str:
            self.new_or_add( ascii_char, results )
        return results


class TestAsciiCounter( unittest.TestCase ):

    def setUp(self):
        self.aclass = AsciiCounter()

    def test_new_or_new_occur(self):
        # arrange
        empty_dict = {} 

        # act
        self.aclass.new_or_add( 'a', empty_dict )

        # assert
        self.assertIn( 'a', empty_dict.keys() )

    def test_new_or_increment_occur(self):
        # arrange
        nonempty_dict = { 'a': 2 } 

        # act
        self.aclass.new_or_add( 'a', nonempty_dict )

        # assert
        self.assertIn( 'a', nonempty_dict.keys() )
        self.assertEqual( nonempty_dict['a'], 3 )

    def test_count_all_empty_string(self):
        # arrange

        # act
        result = self.aclass.count_all( '' )

        # assert
        self.assertIsNotNone( result )
        self.assertFalse( bool(result) )


    def test_count_all_single_string(self):
        # arrange

        # act
        result = self.aclass.count_all( 'abc' )

        # assert
        self.assertIsNotNone( result )
        self.assertTrue( bool(result) )
        self.assertIn( 'a', result.keys() )
        self.assertIn( 'b', result.keys() )
        self.assertIn( 'c', result.keys() )
        for c in [ 'a', 'b', 'c' ]:
            self.assertEqual( result[ c ], 1 )

    def test_count_all_multiple_string(self):
        # arrange

        # act
        result = self.aclass.count_all( 'aabbcc' )

        # assert
        self.assertIsNotNone( result )
        self.assertTrue( bool(result) )
        self.assertIn( 'a', result.keys() )
        self.assertIn( 'b', result.keys() )
        self.assertIn( 'c', result.keys() )
        for c in [ 'a', 'b', 'c' ]:
            self.assertEqual( result[ c ], 2 )


if __name__ == '__main__':
    unittest.main()


