# Каждый из N школьников некоторой школы знает
# Mi языков. Определите, какие языки знают
# все школьники и языки, которые знает
# хотя бы один из школьников.

# Входные данные
schoolboys = 3
schoolboys_1 = [1, 'Russian', 'English']
schoolboys_2 = [2, 'Russian', 'Belarusian', 'English']
schoolboys_3 = [3, 'Russian', 'Italian', 'French']

# Выходные данные
print(schoolboys)
# Выводим количество школьников
result_languages = set(schoolboys_1[1::] + schoolboys_2[1::]
                       + schoolboys_3[1::])
print(result_languages)
# Выводим список всех языков. Для этого
# используем множество, по скольку
# данный тип данных выводит только
# уникальные значения.
result_languages_knowledge = set(schoolboys_1[1::]) \
                             & set(schoolboys_2[1::]) \
                             & set(schoolboys_3[1::])
# Разность трех множеств - это есть языки,
# которые знает хотя бы один школьник
# Выведем для начала количество этих языков
print(len(result_languages_knowledge))
# А затем выведем языки которые
# знает хотя бы один школьник
print(result_languages_knowledge)
