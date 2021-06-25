# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого
# города укажите, в какой стране он
# находится.

# Список стран и городов
input_string1 = 'Russia Moscow Peterburg Novgorod Kaluga'
input_string2 = 'Ukraine Kiew Donetsk Odessa'
# Названия городов
input_string3 = 'Odessa Moscow Novgorod'
# Преобразовываем строки в списки слов
input_list1 = input_string1.split(' ')
input_list2 = input_string2.split(' ')
input_list3 = input_string3.split(' ')
# Создаем словарь где ключем является название
# страны а значием является список городов
new_dict = {input_list1[0]: (input_list1[1::]), input_list2[0]: (input_list2[1::])}
# В данном вдойном цикле мы сравниваем элементы третьего
# цикла с городами для проверки и города в нашем словаре
# и при совпадении значения выводим значение ключа
for i in range(len(input_list3)):
    for k, v in new_dict.items():
        if (isinstance(v, list) and input_list3[i] in v) or input_list3[i] == v:
            print(k)
