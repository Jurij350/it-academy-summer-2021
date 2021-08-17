"""
Тест на функцию smallest_number задачи списка Эйлера
"""

import unittest

import ddt

import task4_eiler


@ddt.ddt
class TestSmallestNumber(unittest.TestCase):

    @ddt.data(
        (2, 6, 2),
        (0, 1, 1),
        (-1, 2, 1)
    )
    @ddt.unpack
    def test_smallest_number(self, a, b, exp_result):
        result = task4_eiler.smallest_number(a, b)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ('a', 2, TypeError),
        ([2], 8, TypeError)

    )
    @ddt.unpack
    def test_smallest_number_error(self, a, b, exp_error):
        with self.assertRaises(exp_error):
            task4_eiler.smallest_number(a, b)


if __name__ == '__main__':
    unittest.main()
