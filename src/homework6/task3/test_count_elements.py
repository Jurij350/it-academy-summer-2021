"""
Функция возвращает элементы которые встречаются только
один раз в списке
"""

import unittest

import ddt

import func_homeworks


@ddt.ddt
class TestCountElementsCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        ([1, 2, 3, 6, 4, 7, 3, 9, 3, 4], [1, 2, 6, 7, 9]),
        ([], []),
        ([0, 0, 0], []),
        (['a'], ['a']),
        (['af', 'af'], []),
        ("1,2,3,4,56,6", ['1', '2', '3', '4', '5'])
    )
    @ddt.unpack
    def test_count_elements(self, new_list, expected_result):
        result = func_homeworks.count_elements(new_list)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (1, TypeError),
        (0, TypeError),
        (None, TypeError)
    )
    @ddt.unpack
    def test_count_elements_error(self, new_list, expected_error):
        with self.assertRaises(expected_error):
            func_homeworks.count_elements(new_list)


if __name__ == '__main__':
    unittest.main()
