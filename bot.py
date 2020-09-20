

def get_status(id):
    status = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&fields=online&access_token=220e8752ae358b036e11a34cc4ec04466e8e55d6c1aea922dfb0ba78759fef10f9ea2a39b9d512444c236&v=5.124')
    return status.json()['response'][0]['online']

def send_msg(message):
    token = '1226847744:AAGu5ZS5Xf3ye9CLQeMNzUC2ouAF43G2Z9g'
    bot = telebot.TeleBot(token)
    bot.send_message('394143446', message)
