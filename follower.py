import telebot
import requests
import vk_api
from datetime import datetime, timezone, timedelta
from time import sleep

vk_session = vk_api.VkApi(
    token='24d8283c15f2794252624bbd8c2a39ff6b8160d7c30bf56e80c27aeaea9f72c2f98e206c4846c4fc13d07')
vk = vk_session.get_api()
offset = timezone(timedelta(hours=3))


def get_status(id):
    return vk.users.get(user_ids=id, fields=['online'])[0]['online']


def send_msg(message):
    token = '1226847744:AAGu5ZS5Xf3ye9CLQeMNzUC2ouAF43G2Z9g'
    bot = telebot.TeleBot(token)
    bot.send_message('394143446', message)


mass = []
while True:
    while True:
        try:
            status = get_status(472177450)
            if status == 1:
                print('Online')
                hours = datetime.now(offset).hour
                minutes = datetime.now(offset).minute
                mass.append([hours, minutes])
                sleep(30)
            else:
                if len(mass) == 0:
                    print('Offline')
                    sleep(30)
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
                    if sess < 0:
                        sess = 0
                    msg = f'Вход - {mass[0][0]}:{mass[0][1]}\nВыход - {mass[-1][0]}:{mass[-1][1]}\nПродолжительность - {sess} минут(ы)'
                    send_msg(msg)
                    print(f'{datetime.now().date()} - Запись завершена')
                    mass.clear()
                    sleep(30)
        except:
            print('Problem')
# 287286283
# 472177450
