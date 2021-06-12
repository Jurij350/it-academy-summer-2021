# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
new_string=str(input('Enter please new string: ')) # Вводим строку для задачи
without_tab_new_string = new_string.replace(" ","")# Удаляем все пробелы

result="".join(set(without_tab_new_string)) # Удаляем все повторяющиеся символы

print (result) # Выводим результат

