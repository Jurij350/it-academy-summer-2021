# Учитывая месяц в виде целого числа от 1 до 12, вернитесь к тому кварталу года, к которому он принадлежит,
# в виде целого числа. Например: месяц 2 (февраль) является частью первого квартала; месяц 6 (июнь) является частью
# второго квартала; и месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    # your code here
    qw = 1
    if 1 <= month <= 3:
        qw = 1
    elif 4 <= month <= 6:
        qw = 2
    elif 7 <= month <= 9:
        qw = 3
    else:
        qw = 4
    return qw
