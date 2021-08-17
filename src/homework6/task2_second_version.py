"""

Создайте декоратор, который вызывает задекорированную функцию пока
она не выполнится без исключений (но не более n раз - параметр
декоратора). Если превышено количество попыток, должно быть
возбуждено исключение типа TooManyErrors

"""

import sqlite3

import mysqlitedatabase


class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class TooManyErrors(Error):
    """Наш сам класс для работы с декоратором"""
    pass


class SqliteCoutner():
    """Класс методы которого считают количество вызовов функции

    Атрибуты класса - счетчик.
    Метод increment записывает в базу данных значение 1 и потом
    считает сумму всех значений.

    """

    def __init__(self):
        self.counter = 0

    def increment(self):
        cursor.execute("INSERT INTO COUNTER (id) VALUES (1)")
        cursor.execute("SELECT SUM(id) from COUNTER where id = 1")
        result_table = cursor.fetchall()
        res_tuple = result_table[0]
        self.counter = res_tuple[0]
        return self.counter


con = sqlite3.connect('database.db')

mysqlitedatabase.sql_table(con)
cursor = con.cursor()


cnt_second = SqliteCoutner()


def dec_counter(func, number=5):
    # Сам декоратор
    def wrapper(*args, **kwargs):
        try:
            if number > cnt_second.counter:
                cnt_second.increment()
            else:
                raise TooManyErrors
            result = func(*args, **kwargs)
            return result
        except TooManyErrors:
            print("Превышено количество попыток вызова функции!")

    return wrapper


@dec_counter
def func_example(n):
    n ** 3
    print(str(n ** 3))


func_example(2)
func_example(3)
func_example(4)
func_example(1)
func_example(6)
func_example(4)
