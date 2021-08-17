"""
Тест функции нахождения цены за товар.
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestCountPriceCase(unittest.TestCase):

    @ddt.data(
        (1, 1, 1, '\rTotal amount: 1 rubles 1 kopeck. '),
        (1, 1, 0, '\rTotal amount: 0 rubles 0 kopeck. '),
        (0, 0, 0, '\rTotal amount: 0 rubles 0 kopeck. '),
        (1, -1, -5, '\rTotal amount: 5 rubles 5 kopeck. ')
    )
    @ddt.unpack
    def test_count_price(self, price_rub, price_cop, count, exp_result):
        result = func_homeworks.count_price(price_rub, price_cop, count)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ("1", 1, 5, TypeError),
        (0, [4], 7, TypeError),
        (6, 5, {'r'}, TypeError),
        ({'a': 6}, 2, 0, TypeError)
    )
    @ddt.unpack
    def test_count_price_error(self, price_rub, price_cop, count, exp_error):
        with self.assertRaises(exp_error):
            func_homeworks.count_price(price_rub, price_cop, count)


if __name__ == '__main__':
    unittest.main()
