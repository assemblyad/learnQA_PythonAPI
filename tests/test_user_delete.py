from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequest


class TestUserDelete(BaseCase):

    # Первый - на попытку удалить пользователя по ID 2. Его данные для авторизации:
    def test_not_allowed_user_deletion(self):
        # LOGIN
        data = {

            'email': 'vinkotov@example.com',

            'password': '1234'

        }

        # url2 = "https://playground.learnqa.ru/api/user/login"
        response2 = MyRequest.post("/api/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")


        # DELETION
        response3 = MyRequest.delete("/api/user/2}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_code_status(response3, 404)

    #Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален:
    def test_allowed_user_deletion(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        # url1 = "https://playground.learnqa.ru/api/user/"
        response1 = MyRequest.post("/api/user/", data=register_data)
        # response1 = requests.post(url1, data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        response2 = MyRequest.post("/api/user/login", data=register_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETION
        response3 = MyRequest.delete(f"/api/user/{user_id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        print(response3.status_code)
        print(response3.content)
        Assertions.assert_code_status(response3, 200)

        # VALIDATE USER DELETION
        response4 = MyRequest.get(f"/api/user/{user_id}")
        Assertions.assert_code_status(response4, 404)

    #Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.
    def test_user_deletion_when_auth_with_other_user(self):
        # LOGIN
        data = {

            'email': 'vinkotov@example.com',

            'password': '1234'

        }

        # url2 = "https://playground.learnqa.ru/api/user/login"
        response1 = MyRequest.post("/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # REGISTER
        register_data = self.prepare_registration_data()
        # url1 = "https://playground.learnqa.ru/api/user/"
        response2 = MyRequest.post("/api/user/", data=register_data)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response2, "id")
        print(user_id)

        # DELETION
        response3 = MyRequest.delete(f"/api/user/{user_id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )

        Assertions.assert_code_status(response3, 400)
