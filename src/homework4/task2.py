# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого
# города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество
# стран N. Далее идет N строк, каждая строка
# начинается с названия страны, затем идут
# названия городов этой страны. В следующей
# строке записано число M, далее идут M запросов —
# названия каких-то M городов, перечисленных
# выше.
# Выходные данные
# Для каждого из запроса выведите название
# страны, в котором находится данный город.
# Примеры
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Выходные данные
# Ukraine
# Russia
# Russia

# Вводим количество стран
number_countries = int(input('Введите '
                             'количество стран '))
# Пустой словарь для записи значений
countries_and_cities_dict = {}
# В цикле записываем в ключе названия
# городов как ключ а название страны - значение
for index in range(0, number_countries):
    countries_for_checks = \
        input('Введите название {}-й страны и городoв: '
              .format(str(index + 1))).split()
    countries_and_cities_dict |= dict.fromkeys(
        countries_for_checks[1:],
        countries_for_checks[0])

# Записываем города в список
check_cities_list = input('Введите через пробел '
                          'названия городов: ').split()

# Через двойной цикл выводим список стран
for index in range(len(check_cities_list)):
    for keys, values in countries_and_cities_dict.items():
        if check_cities_list[index] == keys:
            print(values)
