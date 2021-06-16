# Посчитать количество строчных и прописных букв в веденной строке. Учитывать только английские буквы.
from string import ascii_letters as en

new_str: str = str(input("Enter please string: "))  # Вводим строку для контроля
index_low = 0  # индекс для подсчета строчных букв
index_up = 0  # Индекс для подсчета прописных букв
result = list(new_str)
for i in result:  # Считаем английские буквы в нашем массиве через цикл
    if i.islower() and i in en:
        index_low = index_low + 1
    if i.isupper() and i in en:
        index_up = index_up + 1
print("Lowercase: " + str(index_low))  # Выводим разультат
print("Uppercase: " + str(index_up))
