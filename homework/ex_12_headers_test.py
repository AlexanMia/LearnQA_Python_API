# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
# Этот метод возвращает headers с каким-то значением.
# Необходимо с помощью функции print() понять что за headers и с каким значением,
# и зафиксировать это поведение с помощью assert
import requests


def test_get_header():
    url = 'https://playground.learnqa.ru/api/homework_header'
    response = requests.get(url)
    print(response.headers)
    value_header = 'Some secret value'
    assert value_header == response.headers.get('x-secret-homework-header'), \
        'Value headers is not matched'
