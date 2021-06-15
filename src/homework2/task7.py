# Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника, Если стороны
# определяют треугольник то найти его площадь. Если нет, то вывести сообщение о неверных данных.
print("Please, enter the sides of the triangle: ")
a = int(input())
b = int(input())
c = int(input())
p = 0  # Переменная для вычисления полупериметра
s = 0  # Переменная для вычисления площади
if (a + b) > c and (b + c) > a and (a + c) > b:
    print("\nThe data is entered correctly")
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Square: " + str(s))
else:
    print("Invalid data! ")
