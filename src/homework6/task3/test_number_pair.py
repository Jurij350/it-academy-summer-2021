"""
Тест на функцию которая считает количество пар элементов
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestNumberPairCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        ("1111", 6),
        ("111", 3),
        ([111], 0),
        ({1, 3, 5}, 0),

    )
    @ddt.unpack
    def test_number_pair(self, in_str, expected_result):
        result = func_homeworks.number_pair(in_str)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('mama warit sup', ValueError),
        (0, TypeError),
        (None, TypeError)
    )
    @ddt.unpack
    def test_number_pair_error(self, in_str, expected_error):
        with self.assertRaises(expected_error):
            func_homeworks.number_pair(in_str)


if __name__ == '__main__':
    unittest.main()
