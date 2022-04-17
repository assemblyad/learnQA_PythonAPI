import pytest
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequest

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 =  MyRequest.post("/api/user/login", data=data)
        #response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        #print(response1.headers)
        #print(response1.cookies)
        # assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        # assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")
        # assert "user_id" in response1.json(), "There is user_id the response"

        # self.auth_sid = response1.cookies.get("auth_sid")
        # self.token = response1.headers.get("x-csrf-token")
        # self.user_id_from_auth_method = response1.json()["user_id"]

    def test_user_auth(self):

        response2 = MyRequest.get("/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})
        """
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        """

        # assert "user_id" in response2.json(), "There is no user_id in the second response"
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to the user from check method"
        )

    """
         user_id_from_check_method = response2.json()["user_id"]
         print(user_id_from_check_method)

         assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to the user from check method"
    """

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        # user_id_from_auth_method = response1.json()["user_id"]

        if condition == "no_cookie":
            response2 = MyRequest.get("/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
            """
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
            """
        else:
            condition == "no_token"
            response2 = MyRequest.get("/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
            """                          
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
            """

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )

    """
        assert "user_id" in response2.json(), "There is not user if on the second response"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"
    """
