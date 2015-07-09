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

    def test_convert_all_nothing_was_called(self):
        #
        #  harder to write, let's move on
        #  NOTE: we need two more tests here
        #  1. we need a test that asserts nothing was called
        #
        # ARRANGE
        original_method = Ascii2Ord.to_ordinal
        Ascii2Ord.to_ordinal = MagicMock(return_value=True)

        # ACT
        Ascii2Ord().convert_all('abc')

        # ASSERT
        self.assertEqual(Ascii2Ord.to_ordinal.call_count,3)
        Ascii2Ord.to_ordinal = original_method

    def test_convert_all_return_value_None(self):
        #
        #  harder to write, let's move on
        #  NOTE: we need two more tests here
        #  2. we need a test that asserts None return value
        #
        # ARRANGE
        original_method = Ascii2Ord.to_ordinal
        Ascii2Ord.to_ordinal = MagicMock(return_value=None)

        # ACT
        results = Ascii2Ord().convert_all('junk')

        # ASSERT
        self.assertEqual(Ascii2Ord.to_ordinal.call_count,4)
        self.assertEqual(results,[])
        Ascii2Ord.to_ordinal = original_method

    def test_convert_all_return_multiple_side_effects(self):
        #
        #  harder to write, let's move on
        #  NOTE: we need two more tests here
        #  3. let's look at multiple side effects
        #
        # ARRANGE
        original_method = Ascii2Ord.to_ordinal
        Ascii2Ord.to_ordinal = MagicMock(side_effect=[97,97,None,None])

        # ACT
        results = Ascii2Ord().convert_all('junk')

        # ASSERT
        self.assertEqual(Ascii2Ord.to_ordinal.call_count,4)
        self.assertEqual(results,[97,97])
        Ascii2Ord.to_ordinal = original_method


    def test_convert_all_missing_index_error(self):
        pass

    def test_convert_at_index_result(self):
        pass

    def test_convert_at_index_empty_result(self):
        pass
