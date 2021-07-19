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


def runner(func, my_list, my_list_all):
    if func != None and my_list == None and my_list_all == None:
        print("Функция runner вызывает одну функцию:")
        func
    elif func == None and my_list_all == None and my_list != None:
        for elem in my_list:
            elem
    elif func == None and my_list == None and my_list_all != None:
        for elem in my_list_all:
            elem


"""Функция вызывает одну функцию"""

runner(t_2.count_fib(25), None, None)

"""Функция вызывает несколько функций"""

runner(None, t_2.list_double, None)

"""Функция вызывает все функции"""

runner(None, None, t_2.my_list_all)
