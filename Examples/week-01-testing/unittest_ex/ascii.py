import string
import unittest
import mock
from mock import MagicMock


class Ascii2Ord( object ):
    """
    returns a list of ascii ordinal integers
    """

    def to_ordinal( self, ascii_char ):
        try:
            return ord( ascii_char )
        except TypeError:
            return None

    def convert_all( self, ascii_str ):
        results = []
        for ascii_char in ascii_str:
            ascii_ord = self.to_ordinal( ascii_char )
            if ascii_ord is None:
                continue
            results.append( ascii_ord )
        return results

    def convert_at_index( self, ascii_str, index ):
        results = []
        try:
            results.append( self.to_ordinal( ascii_str[index] ) )
        except IndexError:
            pass
        return results

class TestAscii2Ord( unittest.TestCase ):

    def setUp(self):
        pass

    def test_convert_return_ord(self):
        pass

    def test_convert_return_none_type_error(self):
        pass

    def test_convert_all_every_result(self):
        pass

    def test_convert_all_missing_result(self):
        #
        #  harder to write, let's move on
        #  NOTE: we need two more tests here
        #  1. we need a test that asserts nothing was called
        #  2. we need a test that asserts None return value
        #  3. let's look at multiple side effects
        #  4. let's look at Spy's
        #  5. Note that the spy has assertions too
        #
        pass

    def test_convert_all_missing_index_error(self):
        pass

    def test_convert_at_index_result(self):
        pass

    def test_convert_at_index_empty_result(self):
        pass
