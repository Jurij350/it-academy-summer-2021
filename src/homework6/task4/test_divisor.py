"""
Тест на поиск максимального делителя
являющегося степенью двойки
"""

import unittest

import ddt

import task4


@ddt.ddt
class TestDivisorCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        (28, 4),
        (0, 0),
        (-1, 0),
        (1, 1),
    )
    @ddt.unpack
    def test_divisor(self, number, exp_result):
        result = task4.divisor(number)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ("g", TypeError),
        ([1], TypeError),
        ({'r'}, TypeError),
        (('fg',), TypeError),
        ({'a': 6}, TypeError),
        ('', TypeError),
        (None, TypeError)
    )
    @ddt.unpack
    def test_divisor_error(self, number, exp_error):
        with self.assertRaises(exp_error):
            task4.divisor(number)


if __name__ == '__main__':
    unittest.main()
