# Даны два списка чисел. Посчитайте, сколько
# различных чисел
# входит только в один из этих списков
from random import randint

# Создаем 2 списка случайных чисел
new_different_1 = [randint(0, 36) for i in range(27)]
new_different_2 = [randint(0, 37) for i in range(18)]
# Преобразовываем эти списки в множества
# и делаем симметричную разность этих чисел
new_set1 = set(new_different_1)
new_set2 = set(new_different_2)
new_set1 = new_set1 ^ new_set2
# Выводим результат
print(len(new_set1))
