"""
Тест на функцию check_fraction задачи списка Эйлера
"""

import unittest

import ddt

import task4_eiler


@ddt.ddt
class TestCheckFraction(unittest.TestCase):

    @ddt.data(
        (1, 2, True),
        (2, 4, False),
        (50, 100, False),
        (0, 7, False),
        (-5, 10, False)
    )
    @ddt.unpack
    def test_check_fraction(self, n, d, exp_result):
        result = task4_eiler.check_fraction(n, d)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ('a', 2, TypeError),
        ((2,), [6], TypeError),

    )
    @ddt.unpack
    def test_check_fraction_error(self, n, d, exp_error):
        with self.assertRaises(exp_error):
            task4_eiler.check_fraction(n, d)


if __name__ == '__main__':
    unittest.main()
