# List practice
# 1.Используйте генератор списков чтобы получить
# следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2.Используйте на предыдущий список slice чтобы
# получить следующий: ['ab', 'ad', 'bc'].
# 3.Используйте генератор списков чтобы получить
# следующий['1a', '2a', '3a', '4a'].
# 4.Одной строкой удалите элемент '2a' из
# прошлого списка и напечатайте его.
# 5.Скопируйте список и добавьте в него элемент
# '2a' так чтобы в исходном списке этого
# элемента не было.
correct_list = ['a' + x for x in "bcd"] + \
               ['b' + x for x in "bcd"]
print(correct_list)
correct_list2 = correct_list[::2]
print(correct_list2)
correct_list3 = [x + 'a' for x in '1234']
print(correct_list3)
print(correct_list3.pop(1))
# Удаляем первый элемент и распечатываем его
print(correct_list3)
correct_list4 = correct_list3.copy()
# копируем список и добавляем к нему элемент 2а на
# прежнее место
correct_list4.insert(1, '2a')
print(correct_list4)
