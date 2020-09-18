import requests

response = "https://api.vk.com/method/friends.get?access_token=d6dfd84bd6dfd84bd6dfd84ba8d6b894e3dd6dfd6dfd84b8adc11e47db9aa98b737afb3&user_id=52637246&fields=sex&v=5.53"

response = requests.get(response)

with open('./DataBase/upd_follower.txt', 'r') as file:
    mass = ' '.join([x for x in file])


with open('./DataBase/upd_follower.txt', 'a') as file:
    for x in response.json()['response']['items']:
        if x['sex'] == 2 and not str(x['id']) in mass:
            file.write(f"{x['first_name']} {x['last_name']} - https://vk.com/id{x['id']}\n")

print("Ok")
input()
