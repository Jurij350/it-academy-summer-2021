"""
Тест на функцию нахождения различных слов в
заданной строке.
"""
import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestDifferentWordsCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        ('mama warit sup sup', {'mama', 'warit', 'sup'}),
        ("", {""}),
        ("NAna349/.,.,)))nana", {'NAna', 'nana'})
    )
    @ddt.unpack
    def test_different_words(self, new_string, expected_result):
        result = func_homeworks.different_words(new_string)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (133, TypeError)
    )
    @ddt.unpack
    def test_different_words_error(self, new_string, expected_error):
        with self.assertRaises(expected_error):
            func_homeworks.different_words(new_string)


if __name__ == '__main__':
    unittest.main()
