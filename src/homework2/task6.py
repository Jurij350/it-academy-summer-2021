# Определить является ли число палиндромом (читается слева направо и справа налево одинаково) Число положительное
# целое, произвольной длины. Задачатребует работать только с числами(без конвертации числа в строку или что-нибудь
# еще)
num = int(input("Enter please number: "))
num_one = 0  # данное обратное число мы будем считать с помощью цикла.
index = num  # Промежуточное значение которое будет изменяться каждый раз чтобы вычислить обратное число в цикле
while index != 0:
    ostat_zn = index % 10
    num_one = num_one * 10 + ostat_zn
    index = index // 10
if num == num_one:  # Сравниваем два числа и делаем вывод
    print("Palindrome")
else:
    print("Not a Palindrome")
