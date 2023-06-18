from unittest import TestCase
from unittest.mock import patch

from api_ninja.weather import send_request_temperature



class ProviderAPINinjaTestCase(TestCase):

    def setUp(self) -> None:
        self.get_requests_patch = patch('api_ninja.weather.requests.get')

        self.get_requests_mock = self.get_requests_patch.start()

        self.city = 'Acapulco'
        self.country = 'Mexico'

    def tearDown(self) -> None:
        self.get_requests_patch.stop()

    def test_get_temperature_successfully(self):
        self.get_requests_mock.json.return_value = {"cloud_pct": 90, "temp": 36, "feels_like": 39, "humidity": 38,
                                                "min_temp": 36, "max_temp": 36, "wind_speed": 3.5, "wind_degrees": 213, "sunrise": 1686916850, "sunset": 1686964075}
        self.get_requests_mock.status_code = 200
        response = send_request_temperature(city=self.city, country=self.country)

        self.assertIsNotNone(response)

    def test_get_temperature_fail(self):
        self.get_requests_mock.status_code = 500

        response = send_request_temperature(city=self.city, country=self.country)

        self.assertEqual(response, [])
