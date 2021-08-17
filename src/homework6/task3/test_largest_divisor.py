"""Тест на функцию найбольшего делителя"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestLargestDivisorCase(unittest.TestCase):

    @ddt.data(
        (1, 1, 1),
        (2, 0, 2),
        (0, 5, 5),
        (24, 36, 12),
        (-1, 5, 'Некорректные значения!'),
        (-1, 3, 'Некорректные значения!'),
        (0, 0, 0),
        (-1, -1, 'Некорректные значения!')
    )
    @ddt.unpack
    def test_largest_divisor(self, a, b, exp_result):
        result = func_homeworks.largest_divisor(a, b)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ('1', 6, TypeError),
        (5, [6], TypeError),
        ('1', {'f'}, TypeError),
        ('f', 6, TypeError),
        ('', '', TypeError)
    )
    @ddt.unpack
    def test_largest_divisor_error(self, a, b, exp_error):
        with self.assertRaises(exp_error):
            func_homeworks.largest_divisor(a, b)


if __name__ == '__main__':
    unittest.main()
