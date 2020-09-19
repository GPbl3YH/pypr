import telebot

token = '1226847744:AAGu5ZS5Xf3ye9CLQeMNzUC2ouAF43G2Z9g'
bot = telebot.TeleBot(token)

def send_msg(message):
    bot.send_message('394143446', message)