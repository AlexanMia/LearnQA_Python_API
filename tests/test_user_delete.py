from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):
    """
    У нас есть метод, который удаляет пользователя по ID - DELETE-метод https://playground.learnqa.ru/api/user/{id}
    Само собой, удалить можно только того пользователя, из-под которого вы авторизованы.
    Необходимо в директории tests/ создать новый файл test_user_delete.py с классом TestUserDelete.
    Там написать следующие тесты.
    Первый - на попытку удалить пользователя по ID 2. Его данные для авторизации:
             data = {
                 'email': 'vinkotov@example.com',
                 'password': '1234'
             }
    Убедиться, что система не даст вам удалить этого пользователя.
    Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить,
    затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.
    Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.
    """

    def test_delete_user_by_id_2(self):
        """
        Первый - на попытку удалить пользователя по ID 2. Его данные для авторизации:
             data = {'email': 'vinkotov@example.com',
             'password': '1234'
             }
        Убедиться, что система не даст вам удалить этого пользователя.
        """
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
            f"Unexpected response content {response3.content}"

    def test_delete_just_created_user(self):
        """
        Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить,
        затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.
        """
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        # GET

        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == f"User not found", \
            f"Unexpected response content {response4.content}"

    def test_delete_user_by_auth_another_user(self):
        """
        Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.
        """
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 400)
