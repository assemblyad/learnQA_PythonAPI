import requests
import pytest
import json


class TestCheckUserAgent:
    data = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile",
            "No",
            "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile",
            "Chrome",
            "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot",
            "Unknown",
            "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Googlebot",
            "Chrome",
            "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile",
            "No",
            "iPhone"
        )
    ]

    @pytest.mark.parametrize('agent, platform, browser, device', data)
    def test_check_agent(self, agent, platform, browser, device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"user-agent": agent}

        response = requests.get(url, headers=data)
        obj = json.loads(response.text)
        """
        print(response.status_code)
        print(response.content)
        print(response.text)
        print(response)
        """
        response_browser_name = obj.get("browser")
        response_device_name = obj.get("device")
        response_platform_name = obj.get("platform")

        assert response_browser_name == browser, f"The request with User Agent {agent} return incorrect browser name {response_browser_name}"
        assert response_device_name == device, f"The request with User Agent {agent} return incorrect browser name {response_device_name}"
        assert response_platform_name == platform, f"The browser name is unknown while expected name {response_platform_name}"

        """
        print(response.json())
        print(response.request.headers)
        platform = response.json()['platform']
        browser = response.json()['browser']
        device = response.json()['device']

        assert platform == expected_result_dict[platform], f"The platform ddoes not match"
        assert browser == expected_result_dict[browser], f"The browser does not match"
        assert device == expected_result_dict[device], f"The device does not match"
        """
