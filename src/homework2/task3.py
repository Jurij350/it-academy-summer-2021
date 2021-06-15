# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
new_string = str(input('Enter please new string: '))  # Вводим строку для задачи
without_tab_new_string = new_string.replace(" ", "")  # Удаляем все пробелы

result = str("".join(set(without_tab_new_string)))  # Удаляем все повторяющиеся символы
b = sorted(result)  # Переводим строку в список и сортируем по алфавиту согласно условия
c = ''.join(b)  # Переводим список обратно в строку символов
print(c)  # Выводим результат
