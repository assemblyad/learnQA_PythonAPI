import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequest


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        """
        url = "https://playground.learnqa.ru/api/user/"
        
        response = requests.post(url, data=data)
        """
        response = MyRequest.post("/api/user/", data=data)

        Assertions.assert_code_status(response, response.status_code) == 200
        # print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        """
        url = "https://playground.learnqa.ru/api/user/"
        """

        response = MyRequest.post("/api/user/", data=data)

        # response = requests.post(url, data=data)

        print(response.status_code)
        print(response.content)
        print(response.text)
        print(response)

        Assertions.assert_code_status(response, response.status_code) == 400
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    # Ex15: Тесты на метод user
    # - Создание пользователя с некорректным email - без символа @
    def test_create_user_not_successfully_without_at_sign(self):
        data = self.prepare_registration_data_with_no_at_sign()
        """
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)
        """
        response = MyRequest.post("/api/user/", data=data)

        # print(response.status_code)
        Assertions.assert_code_status(response, response.status_code) == 400
        # print(response.content)
        assert response.content.decode(
            "utf-8") == "Invalid email format", "Unexpected e mail format provided to test without @ sign"
        # Assertions.assert_json_has_key(response, "id")

    # - Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя
    data = [
        (
            "",
            "learnQA",
            "Alex",
            "Demi",
            "test@learnQA.com"
        ),
        (
            "123",
            "",
            "Alex",
            "Demi",
            "test@learnQA.com"
        ),
        (
            "123",
            "learnQA",
            "",
            "Demi",
            "test@learnQA.com"
        ),
        (
            "123",
            "learnQA",
            "Alex",
            "",
            "test@learnQA.com"
        ),
        (
            "123",
            "learnQA",
            "firstName",
            "lastName",
            ""
        )
    ]

    @pytest.mark.parametrize('password, username, firstName, lastName , email', data)
    def test_create_user_not_successfully_with_missing_part_of_registration(self, password, username, firstName, lastName, email):

        #email1 = self.prepare_registration_data(email)['email']

        #print(email)
        data = {
            'password': password,
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email
        }
        """
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)
        """
        response = MyRequest.post("/api/user/", data=data)

        #print(response.status_code)

        Assertions.assert_code_status(response, response.status_code) == 400

        #print(response.content)

        if password is None:
            assert response.content.decode("utf-8") == "The value of 'password' field is too short", "Not empty password provided for the test"
        if username is None:
            assert response.content.decode("utf-8") == "The value of 'username' field is too short", "Not empty username provided for the test"
        if firstName is None:
            assert response.content.decode("utf-8") == "The value of 'firstName' field is too short", "Not empty firstName provided for the test"
        if lastName is None:
            assert response.content.decode("utf-8") == "The value of 'lastName' field is too short", "Not empty lastName provided for the test"
        if email is None:
            assert response.content.decode("utf-8") == "The value of 'email' field is too short", "Not empty email provided for the test"

#- Создание пользователя с очень коротким именем в один символ
    def test_create_user_with_single_char_name(self):
        data = self.prepare_registration_data()
        username1 =data['username'][:1]
        data['username'] = username1
        print(data)

        """
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)
        """
        response = MyRequest.post("/api/user/", data=data)
        #print(response.status_code)
        #print(response.content)

        Assertions.assert_code_status(response, response.status_code) == 400
        assert response.content.decode(
            "utf-8") == "The value of 'username' field is too short", "Not empty username provided for the test"
#- Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_250_chars(self):
        data = self.prepare_registration_data()
        username1 =data['username'][:1]*251
        data['username'] = username1
        #print(data)

        """
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)
        """
        response = MyRequest.post("/api/user/", data=data)
        #print(response.status_code)
        #print(response.content)

        Assertions.assert_code_status(response, response.status_code) == 400
        assert response.content.decode(
            "utf-8") == "The value of 'username' field is too long", "Provided too long user name tot test"
