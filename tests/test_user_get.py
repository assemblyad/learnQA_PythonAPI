import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequest

class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        """
        url = "https://playground.learnqa.ru/api/user/2"
        response = requests.get(url)
        """
        response = MyRequest.get("/api/user/2")
        print(response.content)
        print(response.text)

        Assertions.assert_json_has_key(response,"username")
        Assertions.assert_json_has_not_key(response,"email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        """
        url1 = "https://playground.learnqa.ru/api/user/login"
        response1 = requests.post(url1, data=data)
        """
        response1 = MyRequest.post("/api/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        """
        url2 = f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}"
        response2 = requests.get(url2, headers ={"x-csrf-token": token}, cookies ={"auth_sid":auth_sid})
        """
        response2 = MyRequest.get(f"/api/user/{user_id_from_auth_method}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    def test_get_user_details_with_wrong_user_id(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequest.post("/api/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        """
        url2 = f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}"
        response2 = requests.get(url2, headers ={"x-csrf-token": token}, cookies ={"auth_sid":auth_sid})
        """
        response2 = MyRequest.get(f"/api/user/1", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")