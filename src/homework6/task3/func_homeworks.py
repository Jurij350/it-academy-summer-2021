"""
Оформите указанную задачу из прошлых домашних в виде функции
и покройте тестами. Учтите, что в функцию могут быть переданы
некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные
ситуации сама.
"""


def count_price(price_rub, price_cop, count):
    # Функция считает сумму товара в рублях и копейках
    # при переданном значении количества товара и указанной
    # начальной стоимости
    price_cop = abs(price_cop)
    price_rub = abs(price_rub)
    count = abs(count)
    price_in_kopeck = price_rub * 100 + price_cop
    price_finish = price_in_kopeck * count
    return ("\rTotal amount: {0} rubles {1} kopeck. ".
            format(str(price_finish // 100),
                   str(price_finish % 100)))


def fibonashi(n):
    # Функция вычисляет число ряда Фибоначчи
    if n <= 1:
        return 0
    if n == 2:
        return 1
    n_1 = fibonashi(n - 1)
    n_2 = fibonashi(n - 2)
    n = n_1 + n_2
    return n


def number_pair(in_str):
    # Функция считает количество пар элементов
    in_list = list(in_str)
    in_list = [int(n) for n in in_list if n != ' ']
    index = 0
    for i in range(len(in_list)):
        for j in range(i + 1, len(in_list)):
            if in_list[i] == in_list[j]:
                index = index + 1
    return index


def count_elements(new_list):
    # Функция выводит элементы которые
    # встречаются один раз
    result_list = []
    for i in new_list:
        if new_list.count(i) == 1:
            result_list.append(i)
    return result_list


def largest_divisor(a, b):
    # Функция находит найбольший делитель из двух чисел
    if a < 0 or b < 0:
        return 'Некорректные значения!'
    else:
        while a != 0 and b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            return b
        else:
            return a


def different_words(new_string):
    # Функция находит сколько различных слов в строке
    result_string = ''
    for char in new_string:
        if char.isalpha():
            result_string = result_string + char
        else:
            result_string = result_string + ' '
    result_string = (' '.join(result_string.split()))
    result_list = result_string.split(' ')
    result_set = set(result_list)
    return result_set


def cat_dog_years(human_years):
    # Функция считает возраст собаки и кошки
    # исходя из возраста человека
    cat_years = 0
    dog_years = 0
    result = []
    if human_years == 1:  # путем ветвления выполняем алгоритм
        cat_years = 15
        dog_years = 15
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        return result
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        return result
    elif human_years > 2:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        return result  # Выводим результат
    else:
        return (" Incorrect data! ")


def square_digits(num):
    # в данной задаче необходимо ввести в квадрат
    # все цивры числа и посчитать их сумму
    out = ''
    for im in str(num):
        out = out + str(int(im) ** 2)
    return int(out)


def pair_square(num):
    # Функция возвращает два
    # идеальных квадрата больше и меньше заданного числа
    less_number = num - 1
    more_number = num + 1
    if 0 < num < 1000000:
        while (more_number ** 0.5) % 1 != 0:
            more_number = more_number + 1
        while (less_number ** 0.5) % 1 != 0:
            less_number = less_number - 1
        return '{0}-{1}'.format(str(more_number), str(less_number))


def quarter_of(month):
    # Функция возвращает номер квартала года
    # в зависимости от месяца
    qw = 0
    if 1 <= month <= 3:
        qw = 1
    elif 4 <= month <= 6:
        qw = 2
    elif 7 <= month <= 9:
        qw = 3
    elif 10 <= month <= 12:
        qw = 4
    return qw
