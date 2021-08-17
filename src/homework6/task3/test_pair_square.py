"""
Тест функции нахождения двух идеальных
квадратов больше и меньше заданного числа.
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestPairSquareCase(unittest.TestCase):

    @ddt.data(
        (100, "121-81"),
        (1, "4-0"),
        (-1, None),
        (0, None),
        (15, "16-9")

    )
    @ddt.unpack
    def test_pair_square(self, num, expected_result):
        result = func_homeworks.pair_square(num)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("16", TypeError),
        ([8], TypeError),
        ({7}, TypeError)
    )
    @ddt.unpack
    def test_pair_square_error(self, num, exp_error):
        with self.assertRaises(exp_error):
            func_homeworks.pair_square(num)


if __name__ == '__main__':
    unittest.main()
