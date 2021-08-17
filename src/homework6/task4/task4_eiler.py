"""
Рассмотрим дробь n/d, где n и d являются натуральными числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.
Если перечислить множество сокращенных правильных дробей для d ≤ 8 в
порядке возрастания их значений, получим:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
Нетрудно заметить, что дробь 2/5 расположена непосредственно слева
от дроби 3/7.Перечислив множество сокращенных правильных дробей для
d ≤ 1 000 000 впорядке возрастания их значений, найдите числитель
дроби, расположенной непосредственно слева от дроби 3/7
"""


def smallest_number(a, b):
    """Данная функция находит числитель правильной сокращенной
    дроби из двух чисел
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a


def check_fraction(n, d):
    """Проверка того что дробь сокращена"""
    return n < d and smallest_number(n, d) == 1


def search_fraction_members(max_del):
    """Функция нахождения членов дроби"""
    fraction_left = [1, max_del, 1 / max_del]

    for d in range(3, max_del + 1):
        n = (3 * d - 1) / 7
        if check_fraction(n, d):
            find = (n, d, n / d)

            if find[2] > fraction_left[2]:
                fraction_left = find
    return fraction_left


def found_fraction(delitel):
    """Для начала находим члены дроби для 8
    а затем для 1000000"""
    fraction = search_fraction_members(8)
    if fraction[0] == 2 and fraction[1] == 5:
        maximum_del = delitel
        fraction = search_fraction_members(maximum_del)
        return ("Для d <= {}, {} - является числителем дроби, которая"
                " расположена непосредственно слева от 3/7."
                .format(maximum_del, int(fraction[0])))


print(found_fraction(1000000))
