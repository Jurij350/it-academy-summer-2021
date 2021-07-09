def tuple_gen():
    dictionary_new = \
        {el: el ** 3
         for el in range(1, 21)}
    print(dictionary_new)


def countries_sities(number_countries):
    countries_and_cities_dict = {}
    for index in range(0, number_countries):
        countries_for_checks = \
            input('Введите название {}-й страны и городoв: '
                  .format(str(index + 1))).split()
        countries_and_cities_dict |= dict.fromkeys(
            countries_for_checks[1:],
            countries_for_checks[0])
    check_cities_list = input('Введите через пробел '
                              'названия городов: ').split()

    for index in range(len(check_cities_list)):
        for keys, values in countries_and_cities_dict.items():
            if check_cities_list[index] == keys:
                print(values)


def counting_numbers_first():
    from random import randint
    new_different_1 = [randint(0, 36) for i in range(27)]
    new_different_2 = [randint(0, 37) for i in range(18)]
    result_list = new_different_1 + new_different_2
    new_set = set(result_list)
    print(len(new_set))


def counting_numbers_second():
    from random import randint
    new_different_1 = [randint(0, 36) for i in range(27)]
    new_different_2 = [randint(0, 37) for i in range(18)]
    new_set1 = set(new_different_1)
    new_set2 = set(new_different_2)
    new_set1 = new_set1 ^ new_set2
    print(len(new_set1))


def scoolboys_knowledge_languages():
    schoolboys_1 = [1, 'Russian', 'English']
    schoolboys_2 = [2, 'Russian', 'Belarusian', 'English']
    schoolboys_3 = [3, 'Russian', 'Italian', 'French']
    result_languages = set(
        schoolboys_1[1::] + schoolboys_2[1::] + schoolboys_3[1::])
    print('Количество языков которые знают все школьники: {}'
          .format(len(result_languages)))
    print('Список всех языков: {}'.format(result_languages))
    result_languages_knowledge = set(
        schoolboys_1[1::]) & set(
        schoolboys_2[1::]) & set(
        schoolboys_3[1::])
    print('Количество языков которые знает хотя '
          'бы один школьник: {}'
          .format(len(result_languages_knowledge)))
    print('Список данных языков: {}'
          .format(result_languages_knowledge))


def different_words():
    new_string = 'mama g warit,sup ma      up. р.d  v d'
    result_string = ''
    for char in new_string:
        if char.isalpha():
            result_string = result_string + char
        else:
            result_string = result_string + ' '
    result_string = (' '.join(result_string.split()))
    result_list = result_string.split(' ')
    result_set = set(result_list)
    print('Количество различных слов в строке равно: {}'
          .format(len(result_set)))


def largest_divisor(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        print('НОД ' + str(b))
    else:
        print('НОД ' + str(a))
