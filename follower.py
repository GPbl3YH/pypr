from datetime import datetime
from time import sleep
from telegram import bot
import requests
import html2text
import lxml.html


mass = []

login = '79150470373'
password = 'Prytkov1980!!'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}
session = requests.session()
data = session.get('https://vk.com/', headers=headers)
page = lxml.html.fromstring(data.content)
form = page.forms[0]
form.fields['email'] = login
form.fields['pass'] = password
response = session.post(form.action, data=form.form_values())
while True:
    while True:
        try:
            url = session.get('https://vk.com/id472177450')
            text = html2text.HTML2Text().handle(url.text)
            if len(text[text.find('заходила'):text.find('назад')]) == 0:
                print('Online')
                hours = datetime.now().hour
                minutes = datetime.now().minute
                mass.append([hours, minutes])
                sleep(15)
            else:
                if len(mass) == 0:
                    print('Offline')
                    sleep(15)
                    break
                else:
                    x = [x for x in text[text.find('заходила'):text.find('назад')] if x.isdigit()]
                    if mass[-1][0] == 0 and mass[0][0] == 23: mass[-1][0] = 24
                    if mass[-1][0] == 0 and mass[0][0] == 22: mass[-1][0] = 24
                    if mass[-1][0] == 1 and mass[0][0] == 23: mass[-1][0] = 25
                    if mass[-1][0] == 1 and mass[0][0] == 22: mass[-1][0] = 25
                    if mass[-1][0] == 2 and mass[0][0] == 23: mass[-1][0] = 26
                    if mass[-1][0] == 2 and mass[0][0] == 22: mass[-1][0] = 26
                    sess = ((mass[-1][0] * 60 + mass[-1][1]) - (mass[0][0] * 60 + mass[0][1])) - int(''.join(x))
                    file = open('./DataBase/follower.txt','a', encoding='utf-8-sig')
                    print('Идёт запись...')
                    msg = 'Была в сети с {mass[0][0]}:{mass[0][1]} по {mass[-1][0]}:{mass[-1][1]} ~~ {sess} минут(ы)'
                    file.write(f'\n{msg}')
                    file.close()
                    bot.send_msg(msg)
                    print('Запись завершена')
                    mass.clear()
        except:
            print("Problem")


