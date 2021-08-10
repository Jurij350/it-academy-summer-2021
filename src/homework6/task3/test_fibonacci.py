"""Тест на функцию Фибоначчи"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class FibonnacciCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (-1, 0),
        (-2, 0),
        (-100, 0)
    )
    @ddt.unpack
    def test_fibonacci(self, n, exp_result):
        result = func_homeworks.fibonashi(n)
        self.assertEqual(result, exp_result)

    @ddt.data(
        ('1', TypeError),
        ([5], TypeError),
        ((23,), TypeError),
        ({'f'}, TypeError),
        ({'a': 6}, TypeError),
        (None, TypeError)
    )
    @ddt.unpack
    def test_fibonacci_error(self, n, exp_error):
        with self.assertRaises(exp_error):
            func_homeworks.fibonashi(n)


if __name__ == '__main__':
    unittest.main()
