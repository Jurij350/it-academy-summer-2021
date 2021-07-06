# Создайте декоратор, который хранит результаты
# вызовов функции (за все время вызовов, не только
# текущий запуск программы)

# Это переменная для звписи вызовов функции

# Сам декоратор который хранит записывает
# данные в наш список
result_list = []


def my_first_dec(func):
    def wrapper(*args, **kwargs):
        global result_list

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


# Вызов функций. По результату мы видим что в
# список добавляется новое значение при следующем
# вызове функции. Соответственно старое значение
# тоже сохраняется
result_func_1 = func_multiply(4)
result_func_2 = func_sum(5)
