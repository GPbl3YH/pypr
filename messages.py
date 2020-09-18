import requests
import vk_api
from time import sleep
from datetime import datetime
import os

session = vk_api.VkApi(token='cc17c7e837d512d709f5b056d7a35e6c45df0a5c229ae87d0235db5ae9cdbee8fc28a1600ce8963f12310')


data = session.method('messages.getLongPollServer', {"need_pts":1,
                                                    "lp_version":2,
                                                    "version":5.92})


while True:
    try:
        response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=40&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()
        updates = response['updates']
        if len(updates[0])>3 and 52637246 in updates[0]:
            file = open('./DataBase/messages.txt', 'a', encoding='utf-8-sig')
            message = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} {updates[0][5]}"
            if len(updates[0][5]) == 0: message = message.strip() + ' Это либо файл, либо картинка, либо пересланное сообщение.'
            file.write("\n\t" + message)
            file.close()
            print('Работает')
        data['ts'] = response['ts']
        print('Работает')
    except (IndexError, KeyError):
        os.system("python messages.py")
        raise SystemExit

#52637246
#{"access_token":"cc17c7e837d512d709f5b056d7a35e6c45df0a5c229ae87d0235db5ae9cdbee8fc28a1600ce8963f12310",
#"expires_in":0,
#"user_id":165086485}
