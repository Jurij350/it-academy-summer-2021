"""
Тест функции которая возвращает номер квартала
в зависимости от месяца
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestQuarterCase(unittest.TestCase):

    @ddt.data(
        (1, 1),
        (5, 2),
        (0, 0),
        (-1, 0),
        (13, 0)
    )
    @ddt.unpack
    def test_quarter(self, month, expected_result):
        result = func_homeworks.quarter_of(month)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("2", TypeError),
        ([7], TypeError),
        ((3,), TypeError),
        ({8}, TypeError)
    )
    @ddt.unpack
    def test_quarter_error(self, month, exp_error):
        with self.assertRaises(exp_error):
            func_homeworks.quarter_of(month)


if __name__ == '__main__':
    unittest.main()
