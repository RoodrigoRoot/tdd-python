from unittest import TestCase
from unittest.mock import patch
from weather.weather import (get_temperatures,
                             temperature_dto,
                             is_valid_city_and_country,
                             is_valid_request_to_get_temperatures,
                            )
from datetime import date, datetime


class WeatherTestCase(TestCase):

    def setUp(self) -> None:
        self.city = 'Acapulco'
        self.country = 'Guerrero'
        self.expected_response_from_provider = {"cloud_pct": 90, "temp": 36, "feels_like": 39, "humidity": 38,
                                                "min_temp": 36, "max_temp": 36, "wind_speed": 3.5, "wind_degrees": 213, "sunrise": 1686916850, "sunset": 1686964075}

    @patch('weather.weather.send_request_temperature')
    def test_get_temperatures_succesfull(self, mock_request_temperature):
        mock_request_temperature.return_value = self.expected_response_from_provider
        expected_response = {
            'max_temperature': 36,
            'min_temperature': 36,
            'temperature': 36,
            'hour': datetime.now().day,
            'date': str(date.today()),
            'success': True,
            'message': 'OK'
        }

        response = get_temperatures(city=self.city, country=self.country)

        self.assertDictEqual(response, expected_response)

    @patch('weather.weather.send_request_temperature')
    def test_not_exists_city_or_country(self, mock_request_temperature):
        mock_request_temperature.return_value = []
        expected_response = {
            'success': False,
            'message': 'The city or country does not exists'
        }

        response = get_temperatures(city=self.city, country=self.country)

        self.assertDictEqual(response, expected_response)

    @patch('weather.weather.send_request_temperature')
    def test_with_city_without_country(self, mock_request_temperature):
        mock_request_temperature.return_value = self.expected_response_from_provider

        expected_response = {
            'message': 'Maybe there is another city with that name',
            'max_temperature': 36,
            'min_temperature': 36,
            'temperature': 36,
            'hour': datetime.now().day,
            'date': str(date.today()),
            'success': True
        }

        response = get_temperatures(city=self.city)
        self.assertDictEqual(response, expected_response)

    def test_format_response(self):
        expected_response = {
            'max_temperature': 36,
            'min_temperature': 36,
            'temperature': 36,
            'hour': datetime.now().day,
            'date': str(date.today()),
            'success': True,
            'message': 'OK'
        }

        response = temperature_dto(self.expected_response_from_provider, message='OK', success=True)

        self.assertDictEqual(response, expected_response)

    def test_is_valid_city_and_country_only_city(self):
        city_country_validated = is_valid_city_and_country(city=self.city)
        self.assertTrue(city_country_validated)

    def test_is_valid_city_and_country(self):
        city_country_validated = is_valid_city_and_country(city=self.city, country=self.country)
        self.assertFalse(city_country_validated)

    def test_validate_requests_success(self):

        response = is_valid_request_to_get_temperatures(response=self.expected_response_from_provider)

        self.assertFalse(response)

    def test_validate_requests_fail(self):

        response = is_valid_request_to_get_temperatures(response={})

        self.assertTrue(response)
