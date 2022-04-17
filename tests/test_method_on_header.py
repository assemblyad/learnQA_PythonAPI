import requests

from lib.my_requests import MyRequest


class TestRequestMethodOnHeader():
    def test_header_validation(self):

        response = MyRequest.get("/api/homework_header")
        #response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        expected_header_name = 'x-secret-homework-header'
        expected_header_value = 'Some secret value'

        assert expected_header_name in response.headers, f"Expected header {expected_header_name} not in the list of headers"
        assert expected_header_value == response.headers[expected_header_name], f"Expected header values {expected_header_value} doesn't match"
