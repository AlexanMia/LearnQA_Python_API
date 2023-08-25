import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

# POST, GET, PUT, DELETE

# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

# Вывод статус код 200, Wrong method provided
resp_get = requests.get(url)
print(resp_get)
print(resp_get.text)

resp_post = requests.post(url)
print(resp_post)
print(resp_post.text)

resp_put = requests.put(url)
print(resp_put)
print(resp_put.text)

resp_delete = requests.delete(url)
print(resp_delete)
print(resp_delete.text)
print('________________________')

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.

# Вывод статус код 400
resp_head = requests.head(url)
print(resp_head)
print(resp_head.text)
print('________________________')

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

# Вывод статус код 200, {"success":"!"}
params = {'method': 'GET'}
resp_get = requests.get(url, params=params)
print(resp_get)
print(resp_get.text)

body = {'method': 'POST'}
resp_post = requests.post(url, data=body)
print(resp_post)
print(resp_post.text)

body = {'method': 'PUT'}
resp_put = requests.put(url, data=body)
print(resp_put)
print(resp_put.text)

body = {'method': 'DELETE'}
resp_delete = requests.delete(url, data=body)
print(resp_delete)
print(resp_delete.text)
print('________________________')

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например, с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса.
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок.
# Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

# Вывод запроса, когда реальный тип запроса не совпадает со значением параметра и сервер отвечает 200 кодом
# DELETE GET {"success":"!"}

request = ['POST', 'GET', 'PUT', 'DELETE']
for i in request:
    for k in request:
        body = {'method': k}
        resp = requests.request(method=i, url=url, params=body, data=body)
        if i != k and 'success' in resp.text or (i == k and 'success' not in resp.text):
            print(i, k)
            print(resp.text)
