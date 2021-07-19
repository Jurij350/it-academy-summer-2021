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


def runner(func, some_function, list_all_function):
    if func is not None and some_function is None and list_all_function is None:
        print("Функция runner вызывает одну функцию:")
        func
    elif func is None and list_all_function is None and some_function is not None:
        for elem in some_function:
            elem
    elif func is None and some_function is None and list_all_function is not None:
        for elem in list_all_function:
            elem


runner(t_4.largest_divisor(4, 6), None, None)
runner(None, t_2.some_function, None)
runner(None, None, t_3.list_all_func)
