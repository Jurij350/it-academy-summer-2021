"""Создайте декоратор, который хранит результаты
вызовов функции (за все время вызовов, не только
текущий запуск программы)
"""

def my_first_dec(func):
    """Это переменная для записи вызовов функции"""
    global result_list
    result_list = []

    # Сам декоратор который хранит записывает
    # данные в наш список

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_list.append(result)
        print(result_list)
        return result

    return wrapper


# Обертка двух функций в декоратор
@my_first_dec
def func_multiply(a):
    return a * a


@my_first_dec
def func_sum(b):
    return b + b


"""Вызов функций.
По результату мы видим что в
список добавляется новое значение при следующем
вызове функции. Соответственно старое значение
тоже сохраняется
"""
result_func_1 = func_multiply(4)
result_func_2 = func_sum(5)
