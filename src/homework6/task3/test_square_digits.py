"""
Тест на функцию которая вводит в квадрат
все цифры числа и выводит сумму
"""

import func_homeworks

import ddt

import unittest


@ddt.ddt
class SquareDigitsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        (0, 0),
        (1, 1),
        (12, 14),


    )
    @ddt.unpack
    def test_square_digits(self, num, exp_res):
        result = func_homeworks.square_digits(num)
        self.assertEqual(result, exp_res)  # add assertion here

    @ddt.data(
        (-1, ValueError),
        (-22, ValueError),
        ('ava', ValueError),
        ([123], ValueError),
        (None, ValueError),

    )
    @ddt.unpack
    def test_square_digits_error(self, num, expected_error):
        with self.assertRaises(expected_error):
            func_homeworks.square_digits(num)


if __name__ == '__main__':
    unittest.main()
