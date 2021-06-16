# Завершите функцию, которая принимает нечетное целое число (0 < n < 1000000),
# которое является разницей между двумя последовательными идеальными квадратами,
# и верните эти квадраты в виде строки в формате "больше-меньше"
num = int(input('Enter number: '))
less_number = num - 1
more_number = num + 1
if 0 < num < 1000000:
    while (more_number ** 0.5) % 1 != 0:
        more_number = more_number + 1
    while (less_number ** 0.5) % 1 != 0:
        less_number = less_number - 1
    print(str(more_number) + '-' + str(less_number))
