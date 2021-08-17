"""

Создайте декоратор, который вызывает задекорированную функцию пока
она не выполнится без исключений (но не более n раз - параметр
декоратора). Если превышено количество попыток, должно быть
возбуждено исключение типа TooManyErrors

"""


class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class TooManyErrors(Error):
    """Наш сам класс для работы с декоратором"""
    pass


class CounterDecRun:
    """Класс в котором будут считаться количество вызовов функции."""
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter = self.counter + 1
        return self.counter


# Экземпляр класса счетчика
cnt = CounterDecRun()


# Сам декоратор
def dec_counter(func, number=5):
    def wrapper(*args, **kwargs):
        try:

            if number > cnt.counter:
                cnt.increment()
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
