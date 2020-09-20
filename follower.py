import telebot
from datetime import datetime
from time import sleep
import requests


def get_status(id):
    status = requests.get(
        f'https://api.vk.com/method/users.get?user_ids={id}&fields=online&access_token=220e8752ae358b036e11a34cc4ec04466e8e55d6c1aea922dfb0ba78759fef10f9ea2a39b9d512444c236&v=5.124')
    return status.json()['response'][0]['online']


def send_msg(message):
    token = '1226847744:AAGu5ZS5Xf3ye9CLQeMNzUC2ouAF43G2Z9g'
    bot = telebot.TeleBot(token)
    bot.send_message('394143446', message)


mass = []
while True:
    while True:
        status = get_status(472177450)
        if status == 1:
            hours = datetime.now().hour
            minutes = datetime.now().minute
            mass.append([hours, minutes])
            sleep(15)
        else:
            if len(mass) == 0:
                sleep(15)
            else:
                if mass[-1][0] == 0 and mass[0][0] == 23:
                    mass[-1][0] = 24
                if mass[-1][0] == 0 and mass[0][0] == 22:
                    mass[-1][0] = 24
                if mass[-1][0] == 1 and mass[0][0] == 23:
                    mass[-1][0] = 25
                if mass[-1][0] == 1 and mass[0][0] == 22:
                    mass[-1][0] = 25
                if mass[-1][0] == 2 and mass[0][0] == 23:
                    mass[-1][0] = 26
                if mass[-1][0] == 2 and mass[0][0] == 22:
                    mass[-1][0] = 26
                sess = ((mass[-1][0] * 60 + mass[-1][1]) -
                        (mass[0][0] * 60 + mass[0][1])) - 5
                msg = f'Вход - {mass[0][0]}:{mass[0][1]}\nВыход - {mass[-1][0]}:{mass[-1][1]}\nПродолжительность - {sess} минут(ы)'
                send_msg(msg)
                print(f'{datetime.now().date()} - Запись завершена')
                mass.clear()
