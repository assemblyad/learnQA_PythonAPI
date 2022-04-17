import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequest


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
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

        login_data = {
            'email': email,
            'password': password
        }

        # url2 = "https://playground.learnqa.ru/api/user/login"
        response2 = MyRequest.post("/api/user/login", data=register_data)
        # response2 = requests.post(url2, data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT

        new_name = "Changed name"
        """
        url3 = f"https://playground.learnqa.ru/api/user/{user_id}"
        response3 = requests.put(url3,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
        )
        """
        response3 = MyRequest.put(f"/api/user/{user_id}",
                                  data={"firstName": new_name},
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )

        Assertions.assert_code_status(response3, 200)

        # GET
        """
        url4 = f"https://playground.learnqa.ru/api/user/{user_id}"
        response4 = requests.get(url4,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
        )
        """
        response4 = MyRequest.get(f"/api/user/{user_id}",
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )
        # print(response4.json())
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    # - Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_user_without_auth(self):
        new_name = "Changed name"

        response3 = MyRequest.put(f"/api/user/2",
                                  data={"firstName": new_name}
                                  )

        Assertions.assert_code_status(response3, 400)

    # - Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_edit_user_details_that_is_not_the_same_as_logged(self):
        # REGISTER FIRST USER
        register_data = self.prepare_registration_data()
        response1 = MyRequest.post("/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        """
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")
        """
        # REGISTER SECOND USER
        register_data2 = self.prepare_registration_data()
        response2 = MyRequest.post("/api/user/", data=register_data2)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user_id2 = self.get_json_value(response2, "id")

        # LOGIN WITH FIRST USER

        response4 = MyRequest.post("/api/user/login", data=register_data)

        auth_sid = self.get_cookie(response4, "auth_sid")
        token = self.get_header(response4, "x-csrf-token")

        # EDIT REGISTERED SECOND  USER

        new_name = "Changed name"
        response4 = MyRequest.put(f"/api/user/{user_id2}",
                                  data={"firstName": new_name},
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )
        Assertions.assert_code_status(response4, 400)

    # - Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
    def test_change_email_to_the_one_without_at_sign_of_the_same_logged_user(self):
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

        email1 = self.prepare_registration_data_with_no_at_sign()
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT

        response3 = MyRequest.put(f"/api/user/{user_id}",
                                  data={"email": email1},
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode(
            "utf-8") == "Invalid email format", "Provided e mail for test has valid format while should not include '@' sign"

    # - Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    def test_change_firstName_of_same_as_logged_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequest.post("/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # LOGIN
        response2 = MyRequest.post("/api/user/login", data=register_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT

        new_name = "C"
        response3 = MyRequest.put(f"/api/user/{user_id}",
                                  data={"firstName": new_name},
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )

        # print(response3.status_code)
        # print(response3.content)

        Assertions.assert_code_status(response3, 400)
        actual_message_validation = self.get_json_value(response3, "error")
        assert actual_message_validation == "Too short value for field firstName"
