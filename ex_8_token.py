import time

import requests

# Наша задача - написать скрипт, который делал бы следующее:
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова,
# убеждался в правильности поля status и наличии поля result

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

# создание задачи
response = requests.get(url)
token = {'token': response.json().get('token')}

# отправка запроса с токеном до готовности задачи и проверка поля статус
response_with_token = requests.get(url, params=token)
print(response_with_token.json())
assert response_with_token.json().get('status') == 'Job is NOT ready', "Fields values don't matched"

# ожидание
time.sleep(20)

# отправка запроса с токеном после готовности задачи и проверка поля result
response_after_waiting = requests.get(url, params=token)
print(response_after_waiting.json())
assert 'result' in response_after_waiting.json(), "Key result is not present"
