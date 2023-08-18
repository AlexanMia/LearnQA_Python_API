import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
resp_1 = response.history
resp_2 = response
# quantity of redirects = 2
print(resp_1)
# redirect url 1
print(resp_1[0].url)
# redirect url 2
print(resp_1[1].url)
# final url
print(resp_2.url)
