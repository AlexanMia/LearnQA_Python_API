import allure
import pytest
import requests

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

@allure.suite("Tests user registration module")
@allure.feature('Tests user registration')
class TestUserRegister(BaseCase):
    @allure.title("Create user - positive")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.title("Create user with existing email - negative")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    # Список тестов:
    # - Создание пользователя с некорректным email - без символа @
    # - Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
    # что отсутствие любого параметра не дает зарегистрировать пользователя
    # - Создание пользователя с очень коротким именем в один символ
    # - Создание пользователя с очень длинным именем - длиннее 250 символов

    @allure.title("Create user with incorrect email - negative")
    def test_create_user_with_incorrect_email(self):
        """
        Создание пользователя с некорректным email - без символа @
        """
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", \
            f"Unexpected response content {response.content}"

    @allure.title("Create user without needed field - negative")
    @pytest.mark.parametrize('needed_field', ['password',
                                              'username',
                                              'firstName',
                                              'lastName',
                                              'email'])
    def test_create_user_without_needed_fields(self, needed_field):
        """
        Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
        что отсутствие любого параметра не дает зарегистрировать пользователя
        """
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        data.pop(f"{needed_field}")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {needed_field}", \
            f"Unexpected response content {response.content}"

    @allure.title("Create user with short name - negative")
    def test_create_user_with_short_name(self):
        """
        Создание пользователя с очень коротким именем в один символ
        """
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        data["firstName"] = 'a'

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", \
            f"Unexpected response content {response.content}"

    @allure.title("Create user with long name - positive")
    def test_create_user_with_long_name(self):
        """
        Создание пользователя с очень длинным именем - длиннее 250 символов
        """
        email = 'vinkif@example.com'
        data = self.prepare_registration_data(email)
        data["firstName"] = ('eodswbwnryvrtzknqcdzyhcbyhhadpvzptqtbhrfvkcoooknvyrgzavxapczvipkchtrbuqpctjycjvpozj'
                             'grtojabwsfzztlkqwixpxcwjrhefuhmkvpalugjusyaucefrozuqpwpemzorsdwvaszamjwcrhdvkkjbxya'
                             'yskyjukpkgbdgoiikakoojobyqzzsbrvzo')

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        assert "id" in response.content.decode("utf-8")
