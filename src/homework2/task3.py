# Вводится строка. Требуется удалить из нее
# повторяющиеся символы и все пробелы.
from collections import OrderedDict

new_string = str(input('Enter please new string: '))
new_string = new_string.replace(' ', '')
new_string = "".join(OrderedDict.fromkeys(new_string))
print(new_string)
