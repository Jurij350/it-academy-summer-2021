# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
new_string = str(input('Enter please new string: '))  # Вводим строку для задачи
result = ""  # Промежуточная строка для вывода результата
for i in range(len(new_string)):  # сравниваем символы в строке записываем в результат
    if i == new_string.find(new_string[i]):
        if new_string[i] != ' ':
            result = result + new_string[i]
print(result)