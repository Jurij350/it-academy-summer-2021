"""
Контрольная работа 5 задача 6 написать тест
"""


def divisor(number):
    # Вводится число. Найти его максимальный
    # делитель, являющийся степенью
    # двойки. 10(2) 16(16), 12(4).
    index = 1
    while number >= index:
        if number % index == 0:
            index = index * 2
        else:
            break
    index = index // 2
    return index


