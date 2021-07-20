"""Функция печатает строку символов согласно условия"""
import task1_hw_2_tasks as t_2
import task1_hw_4_tasks as t_4


def fizzbuzz():
    for i in (range(1, 101)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)


"""Функция создает список"""


def list_pract():
    correct_list = [a + b for a in "ab" for b in "bcd"]
    correct_list2 = correct_list[::2]
    print(correct_list2)
    correct_list3 = [x + 'a' for x in '1234']
    print(correct_list3.pop(1))
    correct_list4 = correct_list3.copy()
    correct_list4.insert(1, '2a')


"""Функция создает кортеж"""


def tuple_pract():
    new_list = ['a', 'b', 'c']
    new_tuple = tuple(new_list)
    print(new_tuple)
    new_tuple1 = ('a', 'b', 'c')
    new_list_1 = list(new_tuple1)
    print(new_list_1)
    a, b, c = 'a', 2, 'python'
    print(a, b, c)
    new_tuple2 = ([1, 2, 3],)
    for x in new_tuple2:
        for new_list in x:
            print(new_list)
    print('Длина кортежа: ' + str(len(new_tuple2)))


"""Функция считает пары чисел"""


def number_pair():
    in_str = '1 1 1 1'
    in_list = list(in_str)
    in_list = [int(n) for n in in_list if n != ' ']
    index = 0
    for i in range(len(in_list)):
        for j in range(i + 1, len(in_list)):
            if in_list[i] == in_list[j]:
                index = index + 1
    print(index)


"""Функция убирает повторяющиеся элементы"""


def count_elements():
    new_list = [2, 4, 5, 3, 3, 5, 6, 7, 5, 4]
    result_list = []
    for i in new_list:
        if new_list.count(i) == 1:
            result_list.append(i)
    print(result_list)


"""Функция преобразовывает список"""


def transformation_num():
    new_list = [1, 3, 6, 0, 0, 4, 5, 6, 3, 0, 0, 0, 6]
    for i in reversed(range(len(new_list))):
        if new_list[i] == 0:
            new_list.append(new_list.pop(i))
    print(new_list)


# Список который содержит в себе все функции для запуска функции runner()

list_all_func = [transformation_num(), count_elements(), number_pair(),
                 tuple_pract(), list_pract(), fizzbuzz(), t_4.tuple_gen(),
                 t_4.counting_numbers_first(), t_4.counting_numbers_second(),
                 t_4.scoolboys_knowledge_languages(t_4.schoolboys_1,
                                                   t_4.schoolboys_2,
                                                   t_4.schoolboys_3),
                 t_4.different_words(),
                 t_4.largest_divisor(24, 101), t_2.count_price(5, 6, 4),
                 t_2.long_word('mama warit sup'),
                 t_2.repeat_symbols('mama warit sup'), t_2.count_symbols('ma wa sup'),
                 t_2.count_fib(25), t_2.palindrome(18), t_2.triangle(3, 5, 7),
                 t_2.number_list(15), t_2.quarter_of(4), t_2.square_digits(5),
                 t_2.cat_dog_years(12), t_2.found_number(5)]
