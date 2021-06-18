# У меня есть кошка и собака.
# Я получил их одновременно с котенком/щенком. Это было много лет назад.
# Верните их соответствующие возрасты теперь как
# [Человеческие годы,кошачьи годы,собачьи годы]
# ЗАПИСИ:
#  Человеческие годы >= 1
#  Человеческие годы-это только целые числа
# Кошачьи Годы
#  15 кошачьих лет за первый год
# +9 кошачьих лет за второй год
# +4 кошачьих года за каждый последующий год
# Собачьи Годы
#  15 собачьих лет за первый год
# +9 собачьих лет за второй год
#  +5 собачьих лет за каждый последующий год.
human_years = int(input(" Enter, please human years "))  # вводим данные
cat_years = 0
dog_years = 0
result = []
if human_years == 1:  # путем ветвления выполняем алгоритм
    cat_years = 15
    dog_years = 15
    result.insert(0, dog_years)
    result.insert(0, cat_years)
    result.insert(0, human_years)
    print(result)
elif human_years == 2:
    cat_years = 15 + 9
    dog_years = 15 + 9
    result.insert(0, dog_years)
    result.insert(0, cat_years)
    result.insert(0, human_years)
    print(result)
elif human_years > 2:
    cat_years = 15 + 9 + (human_years - 2) * 4
    dog_years = 15 + 9 + (human_years - 2) * 5
    result.insert(0, dog_years)
    result.insert(0, cat_years)
    result.insert(0, human_years)
    print(result)  # Выводим результат
else:
    print(" Incorrect data! ")
