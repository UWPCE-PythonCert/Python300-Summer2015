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

    def test_convert_return_ord(self):
        pass

    def test_convert_return_none_type_error(self):
        pass

    def test_convert_all_every_result(self):
        pass

    def test_convert_all_missing_result(self):
        pass

    def test_convert_all_missing_result(self):
        # harder to write, let's move on
        pass

    def test_convert_all_missing_index_error(self):
        pass

    def test_convert_at_index_result(self):
        pass

    def test_convert_at_index_empty_result(self):
        pass
