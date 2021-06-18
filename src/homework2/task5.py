# Выведите n-ое число Фибоначчи, используя
# только временные переменные, циклические операторы и условные операторы.
# n-вводится
n = int(input(" Enter please the number of the fibonacci series: "))
# Ввобдим номер числа Фибоначчи
fib1 = 1  # Значение первых двух членов ряда
fib2 = 1
i = 0  # Начальный индекс
while i < n - 2:  # Через цикл While находим число в ряде
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print("Meaning: ", fib2)
