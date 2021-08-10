"""
Тест на функцию search_fraction_members задачи списка Эйлера
"""

import unittest

import ddt

import task4_eiler


@ddt.ddt
class TestSearchFractionMembers(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        (-1, [1, -1, -1]),
        (2, [1, 2, 0.5]),
        (4, [1, 4, 0.25])
    )
    @ddt.unpack
    def test_search_fraction_members(self, max_del, exp_result):
        result = task4_eiler.search_fraction_members(max_del)
        self.assertEqual(result, exp_result)

    @ddt.data(
        (0, ZeroDivisionError),
        ('d', TypeError),
        ([4], TypeError),
        ((9,), TypeError)
    )
    @ddt.unpack
    def test_search_fraction_members_error(self, max_del, exp_error):
        with self.assertRaises(exp_error):
            task4_eiler.search_fraction_members(max_del)


if __name__ == '__main__':
    unittest.main()
