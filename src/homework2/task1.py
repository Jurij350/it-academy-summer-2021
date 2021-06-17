# Напишите программу, которая считает общую цену. Вводится
# М рублей и N копеек.цена, а также количество S товара.
# Посчитайте общую цену в рублях и копейках за L товаров.

count = int(input('Enter please product quantity: '))
rubles = int(input('Enter please price in rubles: '))
kopecks = int(input('Enter please price in kopecks: '))
price_in_kopecs = rubles * 100 + kopecks  # Переводим рубли в копейки
price_finish = price_in_kopecs * count  # Считаем общую цену товара
print("\rTotal amound: " + str(price_finish // 100)/
      + " rubles " + str(price_finish % 100) + " kopeсks. ")
