"""

Создайте  модель из жизни. Это может быть бронирование
комнаты в отеле, покупка билета в транспортной компании,
или простая РПГ. Создайте несколько объектов классов,
которые описывают ситуацию. Объекты должны содержать
как атрибуты так и методы класса для симуляции различных
действий. Программа должна инстанцировать объекты и
эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.

"""

import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Ticket:
    """Класс Ticket определяет основные действия,
    которые необходимо сделать для покупки билета в аэропорту Атрибуты:
    Откуда where from
    Куда to
    Класс билета comfort level
    День вылета day
    """

    def __init__(self, where_from, to, comfort_level, day):
        """Kонструктор в котором определяются пременные:
        Откуда полет, куда полет, класс билета, день вылета."""

        self.where_from = where_from
        self.to = to
        self.comfort_level = comfort_level
        self.day = day

    @staticmethod
    def health_department():
        #  Проверка температуры на входе в аэропорт
        temp = float(input('Enter, please, your temperature: '))
        if temp <= 36.7:
            answer = 'Please, come in!'
        else:
            answer = 'You must pass the test Covid_19'
        return answer

    @staticmethod
    def price_count(comfort_level):
        # Расчет стоимости билета исходя из класса комфорта
        if comfort_level == 1:
            price = 1500 * 3
        elif comfort_level == 2:
            price = 1500 * 2
        elif comfort_level == 1:
            price = 1500
        return price

    @staticmethod
    def security_service():
        # Проверка службы безопасности на входе
        new_question = str(input("Is there anything forbidden? y/n: "))
        answer = ''
        if new_question == 'y':
            answer = "You can't come"
        if new_question == 'n':
            answer = 'Please come in! '
        return answer

    def order_ticket(self):
        # Заказ билета в кассе
        now = datetime.datetime.now()
        price = Ticket.price_count(self.comfort_level)
        return "You're flying from {} to {}. \n Day {} Price {}. \n {} \n " \
               "We wish you a successful flight!" \
            .format(self.where_from, self.to, self.day, price,
                    now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))

    def buying_ticket(self, e_mail):
        # Покупка билета с отправлением на электронную почту
        # Дата и время осуществления операции
        now = datetime.datetime.now()
        adder_from = "yurystankevi4@yandex.ru"
        adder_to = e_mail
        password = "jycosxoqbyhnxhtq"
        price = Ticket.price_count(self.comfort_level)
        msg = MIMEMultipart()
        msg['From'] = adder_from
        msg['To'] = adder_to
        msg['Subject'] = 'Congratulations! You have bought a ticket'

        body = "You're flying from {} to {}. \n Day {} Price {}. \n{} " \
               "\n We wish you a successful flight!" \
            .format(self.where_from, self.to, self.day, price,
                    now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)

        server.login(adder_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Закрываем вход


if __name__ == '__main__':
    # Этот if для того если я захочу импортировать класс
    # как модуль чтобы нижеописанные операции не выполнялись
    ticket = Ticket('Minsk', 'Warshaw', 1, '26.09.21')
    print(ticket.health_department())
    print(ticket.security_service())
    print(ticket.order_ticket())

    ticket.buying_ticket('jurasach@mail.ru')
