# В рамках этой задачи с помощью pytest необходимо написать тест,
# который просит ввести в консоли любую фразу короче 15 символов.
# А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
# python -m pytest -s ex_10_test.py


def test_len_phrase():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, 'Phrase length is more than 15 symbols'
