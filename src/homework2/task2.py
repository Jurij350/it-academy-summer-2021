
# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания
import re

new_string = (input('Enter please the sentence: '))
# Вводим предложение которое нам предстоит анализировать
correct_string = re.sub(r'[^\w\s]', ' ',
                        new_string)  # Заменим все знаки
# препинания на пробели запишем все это в новую строку
#  Будем использовать re.sub(pattern, replacement, original_string)
#  - библиотеку регулярных выражений
count = max(correct_string.split(), key=len)
# Находим самое длинное слово
print(count)  # Выводим результат
