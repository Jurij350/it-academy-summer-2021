"""
В данном файле создаем таблицу базы данных в
 отдельной функции
"""


from sqlite3 import OperationalError


def sql_table(cont):
    try:
        cursor = cont.cursor()
        cursor.execute("CREATE TABLE COUNTER(id INTEGER)")
        cont.commit()
    except OperationalError:
        print("Таблица уже существует")
