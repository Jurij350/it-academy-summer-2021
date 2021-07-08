# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле
# ./data_hw5/ ratings.list.
# Откройте и прочитайте файл
# (если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла
# top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов,
# years.txt – гистограмма годов.


try:
    # создаем файлы с атрибутом - для записи
    top_250_movies_txt = open('top250_movies.txt', 'w')
    levels_txt = open('levels.txt', 'w')
    years_txt = open('years.txt', 'w')
    # В цикле записываем соответствующую часть строки
    # в отдельные файлы согласно заданию программы
    with open('ratings.txt') as rating_txt:
        for i, line in enumerate(rating_txt):
            if 28 <= i <= 278:
                # Преобразовываем строку в массив
                # символов и записываем последний символ
                years_txt.write(line.split(' ')[-1])
                # Берем срез строки и удаляем из него пробелы
                levels_txt.write((line[27:32]).strip() + '\n')
                #
                top_250_movies_txt.write((line[32:-7]).strip() + '\n')
except IOError as e:
    print(u'Необходимо убедиться '
          u'существует ли файл в '
          u'корневом каталоге ')


finally:
    # В данном блоке закрываем все файлы
    rating_txt.close()
    levels_txt.close()
    years_txt.close()
    top_250_movies_txt.close()
