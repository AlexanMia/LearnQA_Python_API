# Необходимо написать тест, который делает запрос на метод
# Этот метод возвращает какую-то cookie с каким-то значением.
# Необходимо с помощью функции print() понять что за cookie и с каким значением,
# и зафиксировать это поведение с помощью assert
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
import requests


def test_get_cookie():
    url = 'https://playground.learnqa.ru/api/homework_cookie'
    response = requests.get(url)
    print(dict(response.cookies))
    assert dict(response.cookies) == {'HomeWork': 'hw_value'}, 'Cookies is not matched'
