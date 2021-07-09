# Оформите решение задач из прошлых домашних работ
# в функции. Напишите функцию runner.
# (все станет проще когда мы изучим модули,
# getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только
# функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает
# все переданные функции.


# Импортируем все модули из пакета
# где есть функции наших задач
import task1_hw_2_tasks as t_2
import task1_hw_3_tasks as t_3
import task1_hw_4_tasks as t_4
import time


def runner():
    # Все функции из 2 контрольной работы
    t_2.count_price(5, 10, 5)
    t_2.long_word('Mama varit sup')
    t_2.repeat_symbols('mama warit supeC')
    t_2.count_symbols('mama warit sup')
    t_2.count_fib(25)
    t_2.palindrome(2552)
    t_2.triangle(3, 4, 5)
    t_2.number_list(4)
    t_2.quarter_of(4)
    t_2.square_digits(5)
    t_2.cat_dog_years(7)
    t_2.found_number(7)
    # Все функции из 3 контрольной работы
    t_3.fizzbuzz()
    t_3.list_pract()
    t_3.tuple_pract()
    t_3.number_pair()
    t_3.count_elements()
    t_3.transformation_num()
    # Все функции из 4 контрольной работы
    t_4.tuple_gen()
    t_4.countries_sities(2)
    t_4.counting_numbers_first()
    t_4.counting_numbers_second()
    t_4.scoolboys_knowledge_languages()
    t_4.different_words()
    t_4.largest_divisor(112, 2357)

# Функция которая вызывает
# одну функцию


t_3.runner(t_3.number_pair())
time.sleep(3)
# Функция которая вызывает три переданные функии
t_2.runner(t_3.transformation_num(), t_3.count_elements(), t_3.fizzbuzz())
# Функция которая вызывает все функции по очереди
time.sleep(3)
runner()
