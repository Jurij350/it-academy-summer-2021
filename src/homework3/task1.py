#  Напишите программу, которая печатает цифры
#  от 1 до 100, но вместо чисел, кратных 3 пишет
#  Fizz, вместо чисел кратный 5 пишет Buzz,
#  а вместо чисел одновременно кратных и
#  3 и 5 - FizzBuzz
new_list = list(range(1, 101))
for i in new_list:
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
