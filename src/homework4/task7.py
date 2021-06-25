# Даны два натуральных числа. Вычислите их
# найбольший делитель при помощи алгоритма
# Евклида(мы не знаем функцию и рекурсию)
a = int(input(' Введите число №1 :'))
b = int(input(' Введите число №2 :'))
# Через цикл находим НОД
while a != 0 and b != 0:
    if a >= b:
        a = a % b
    else:
        b = b % a
# Через условие выводим результат
if a == 0:
    print('НОД ' + str(b))
else:
    print('НОД ' + str(a))
