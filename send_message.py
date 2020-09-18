import vk_api
import requests
import os
from time import sleep

session = vk_api.VkApi(token='cc17c7e837d512d709f5b056d7a35e6c45df0a5c229ae87d0235db5ae9cdbee8fc28a1600ce8963f12310')
id = 52637246
os.system("cls")

def last_message(id):
    response = session.method('messages.getHistory', {"user_id": id,
                                                  "rev":0,
                                                  "count": 1})
    return response["items"][0]

print(last_message(id)["text"])
while True:
    message = input("Сообщение: ")
    if message.lower() == "close": break
    data = session.method('messages.send', {"user_id":id,
                                            "random_id":last_message(id)['conversation_message_id'],
                                            "message":message})
    print("Сообщение успешно отправлено")
    sleep(1)
