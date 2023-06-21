import requests

from unittest import TestCase, skip
from unittest.mock import patch, Mock

from api_ninja.weather import send_request_temperature



class ProviderAPINinjaTestCase(TestCase):

    def setUp(self) -> None:
        self.get_requests_get_patch = patch('api_ninja.weather.requests')

        self.get_requests_get_mock = self.get_requests_get_patch.start()

        self.expected_json_response = {"cloud_pct": 90, "temp": 36, "feels_like": 39, "humidity": 38,
        "min_temp": 36, "max_temp": 36, "wind_speed": 3.5, "wind_degrees": 213, "sunrise": 1686916850, "sunset": 1686964075}

        self.get_requests_get_mock.get.return_value.json.return_value = self.expected_json_response

        self.city = 'Acapulco'
        self.country = 'Mexico'

    def tearDown(self) -> None:
        self.get_requests_get_mock.stop()

    def test_get_temperature_successfully(self):

        response = send_request_temperature(city=self.city, country=self.country)
        print(response)
        self.assertIsNotNone(response)
        self.assertEqual(response, self.expected_json_response)

    def test_get_temperature_fail(self):
        self.get_requests_get_mock.get.return_value.raise_for_status.side_effect = Exception()

        response = send_request_temperature(city=self.city, country=self.country)

        self.assertEqual(response, {})
