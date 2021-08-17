"""
Тест на функцию которая считает
возраст собаки и кошки исходя из возраста
человека
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestCatDogYearsTestCase(unittest.TestCase):

    @ddt.data(
        (0, " Incorrect data! "),
        (1, [1, 15, 15]),
        (2, [2, 24, 24]),
        (3, [3, 28, 29]),
        (24, [24, 112, 134]),
        (-1, " Incorrect data! ")
    )
    @ddt.unpack
    def test_cat_dog_years(self, human_years, expected_result):
        result = func_homeworks.cat_dog_years(human_years)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (None, TypeError),
        ("5", TypeError),
        ({6}, TypeError),
        ((1,), TypeError)
    )
    @ddt.unpack
    def test_cat_dog_years_error(self, human_years, expected_error):
        with self.assertRaises(expected_error):
            func_homeworks.cat_dog_years(human_years)


if __name__ == '__main__':
    unittest.main()
