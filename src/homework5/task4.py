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
    file_hw = open('ratings.txt')
except IOError as e:
    print(u'Необходимо убедиться '
          u'существует ли файл в '
          u'корневом каталоге ')
else:
    with file_hw as rating_txt :
        lines = rating_txt.readline()

    print(len(lines))

finally:
    rating_txt.close()
