import re


"""Функция считает общую цену товара """
def count_price(price_rub, price_cop, count):
    price_in_kopeck = price_rub * 100 + price_cop
    price_finish = price_in_kopeck * count
    print("\rTotal amount: {0} rubles {1} kopeck. ".
          format(str(price_finish // 100),
                 str(price_finish % 100)))


"""Функция находит самое длинное слово"""
def long_word(new_string):
    correct_string = re.sub(r'[^\w\s]', ' ',
                            new_string)
    count = max(correct_string.split(), key=len)
    print(count)


"""Функция удаляет последующие вхождения символов строки"""
def repeat_symbols(new_string):
    from collections import OrderedDict
    new_string = new_string.replace(' ', '')
    new_string = "".join(OrderedDict.fromkeys(new_string))
    print(new_string)



def count_symbols(new_str):
    index_low = 0
    index_up = 0
    result = list(new_str)
    for i in result:
        if 'a' <= i <= 'z':
            index_low = index_low + 1
        if 'A' <= i <= 'Z':
            index_up = index_up + 1
    print("Lowercase: {} ".format(index_low))
    print("Uppercase: {}".format(index_up))


"""Функция находит число Фибоначчи"""
def count_fib(n):
    def Fib(n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        n_1 = Fib(n - 1)
        n_2 = Fib(n - 2)
        n = n_1 + n_2
        return n

    print(n)


"""Функция проверяет является ли число палиндромом"""
def palindrome(num):
    num_one = 0
    index = num
    while index != 0:
        ostat_zn = index % 10
        num_one = num_one * 10 + ostat_zn
        index = index // 10
    if num == num_one:  # Сравниваем два числа и делаем вывод
        print("Palindrome")  # Число палиндром
    else:
        print("Not a Palindrome")


"""Функция проверяет существует ли треугольник"""
def triangle(a, b, c):
    p = 0
    s = 0
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print("\nThe data is entered correctly")
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("Square: " + str(s))
    else:
        print("Invalid data! ")


"""Функция переворачивает строку"""
def number_list(num):
    result_1 = [int(x) for x in str(num)]
    result_1.sort(reverse=True)
    result = int(''.join(map(str, result_1)))
    print(result)


"""Функция возвращает номер квартала"""
def quarter_of(month):
    qw = 1
    if 1 <= month <= 3:
        qw = 1
    elif 4 <= month <= 6:
        qw = 2
    elif 7 <= month <= 9:
        qw = 3
    else:
        qw = 4
    return qw


"""Функция возвращает квадрат цифр числа"""
def square_digits(num):
    out = ''
    for im in str(num):
        out = out + str(int(im) ** 2)
    return int(out)


""" Функция считает возраст кота и собаки исходя из возраста человека"""
def cat_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    result = []
    if human_years == 1:
        cat_years = 15
        dog_years = 15
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        print(result)
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        print(result)
    elif human_years > 2:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
        result.insert(0, dog_years)
        result.insert(0, cat_years)
        result.insert(0, human_years)
        print(result)  # Выводим результат
    else:
        print(" Incorrect data! ")


""" Функция возвращает корни квадратные рядом стоящих чисел"""
def found_number(num):
    less_number = num - 1
    more_number = num + 1
    if 0 < num < 1000000:
        while (more_number ** 0.5) % 1 != 0:
            more_number = more_number + 1
        while (less_number ** 0.5) % 1 != 0:
            less_number = less_number - 1
    print('{}-{}'.format(str(more_number), str(less_number)))


def runner(func_1, func_2, func_3):
    func_1
    func_2
    func_3
