# Выведите n-ое число Фибоначчи, используя
# только временные переменные, циклические операторы и условные операторы.
# n-вводится
n = int(input(" Enter please the number of the fibonacci series: "))


def Fib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    n_1 = Fib(n - 1)
    n_2 = Fib(n - 2)
    n = n_1 + n_2
    return n


# данную задачу решил через рекурсивную функцию
# которая вызывает сама себя

print(Fib(n))
