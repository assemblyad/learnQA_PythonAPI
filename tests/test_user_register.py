import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)

        Assertions.assert_code_status(response, response.status_code) == 200
        #print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        url = "https://playground.learnqa.ru/api/user/"

        response = requests.post(url, data=data)

        print(response.status_code)
        print(response.content)
        print(response.text)
        print(response)

        Assertions.assert_code_status(response, response.status_code) == 400
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"


#https://playground.learnqa.ru/api/user/{id}