import pytest
import requests

class TestRequestUserAgent():
    user_agent = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    expected_result_dict = [
        ("'platform': 'Mobile', 'browser': 'No', 'device': 'Android'"),
        ("'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'"),
        ("'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'"),
        ("'platform': 'Web', 'browser': 'Chrome', 'device': 'No'"),
        ("'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'")
    ]

    @pytest.mark.parametrize('user_agent', user_agent, 'expected_result_dict', expected_result_dict)
    def test_header_validation(self, user_agent, expected_result_dict):
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check"
            ,headers={"User-Agent": user_agent}
        )

        print(response.json())
        print(response.request.headers)
        platform = response.json()['platform']
        browser = response.json()['browser']
        device = response.json()['device']

        assert platform == expected_result_dict[platform], f"The platform ddoes not match"
        assert browser == expected_result_dict[browser], f"The browser does not match"
        assert device == expected_result_dict[device], f"The device does not match"
