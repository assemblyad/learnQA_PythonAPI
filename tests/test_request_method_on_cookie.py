import requests
from lib.my_requests import MyRequest

class TestRequestMethodOnCookie():
    def test_cookie_validation(self):
        response1 = MyRequest.get("/api/homework_cookie")
        #response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response1.cookies)
        expected_cookie_name = 'HomeWork'
        expected_cookie_value = 'hw_value'

        assert expected_cookie_name in response1.cookies, f"Expected cookie {expected_cookie_name} not found in the returned list of cookies"
        assert expected_cookie_value == response1.cookies[expected_cookie_name], f"Expected cookie values {expected_cookie_value} doesn't match"

