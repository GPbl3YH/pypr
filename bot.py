from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot
import vk_api

token = '1226847744:AAGu5ZS5Xf3ye9CLQeMNzUC2ouAF43G2Z9g'
bot = telebot.TeleBot(token)

vk_session = vk_api.VkApi(
    token='529239d88d367cfdb39fa8527eda052d6286d4724bec5c5b90a64b7dd110245049ddf2084523085725784')
vk = vk_session.get_api()

@bot.message_handler(commands=['start']) #/start - Главное меню
def handle_start(message):
    user_markup = ReplyKeyboardMarkup(True, one_time_keyboard=False)
    user_markup.row('/status')
    bot.send_message(message.from_user.id, 'Successful',reply_markup=user_markup)

@bot.message_handler(commands=['status']) #/start - Главное меню
def handle_status(message):
    status = 'Online' if vk.users.get(user_ids=472177450, fields=['online'])[0]['online'] == 1 else 'Offline'
    bot.send_message(message.from_user.id, status, reply_markup=False)


bot.polling()

