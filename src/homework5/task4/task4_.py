"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле
./data_hw5/ ratings.list.
Откройте и прочитайте файл
(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

from collections import Counter

try:
    # В цикле записываем соответствующую часть строки
    # в отдельные файлы согласно заданию программы
    # Данные два списка необходимы для
    # промежуточных значений

    result_years = []
    result_levels = []
    with open('ratings.txt') as rating_txt:
        with open('top250_movies.txt','w') as top_250_movies_txt:
            for i, line in enumerate(rating_txt):
                if 28 <= i <= 278:
                    # Преобразовываем строку в массив
                    # символов и записываем последний
                    # символ в список
                    result_years.append(((line.split(' ')[-1])[1:5]))
                    # Берем срез строки и удаляем из него
                    # пробелы и записываем это все в список
                    result_levels.append((line[27:32]).strip())
                    # записываем в файл список всех названий фильмов
                    top_250_movies_txt.write((line[32:-7]).strip() + '\n')

    # Через Counter записываем гистограмму готов в файл
    # используем контекстный менеджер
    result_years.sort(reverse=True)
    with open('years.txt', 'w') as years_txt:
        for number, count in Counter(result_years).items():
            if count > 1:
                years_txt.write(f"Год выхода {number} вышло "
                                f"{count} фильма(ов)\n")

    # Через Counter записываем гистограмму рейтингов в файл
    # используем контекстный менеджер
    with open('levels.txt', 'w') as levels_txt:
        for number, count in Counter(result_levels).items():
            if count > 1:
                levels_txt.write(f"Рейтинг {number} "
                                 f"составляет {count} фильм(ов)\n")


except IOError:
    print(u'Необходимо убедиться '
          u'существует ли файл в '
          u'корневом каталоге ')


finally:
    # В данном блоке закрываем все файлы
    rating_txt.close()
    levels_txt.close()
    years_txt.close()
    top_250_movies_txt.close()
