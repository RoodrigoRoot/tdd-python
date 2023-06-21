from typing import Optional
from datetime import date, datetime

from api_ninja.weather import send_request_temperature


def get_temperatures(city: str, country: Optional[str]=None):
    message = 'OK'
    success = True

    if is_valid_city_and_country(city=city, country=country):
        message = 'Maybe there is another city with that name'

    response_temperatures = send_request_temperature(city=city, country=country)

    if is_valid_request_to_get_temperatures(response=response_temperatures):
        return {
                'success': False,
                'message': 'The city or country does not exists'
            }

    return temperature_dto(response_temperatures, message, success)


def is_valid_city_and_country(city: str, country: Optional[str]=None) -> bool:
    return not bool(city and country)


def is_valid_request_to_get_temperatures(response: dict) -> bool:
    return not response


def temperature_dto(temperature_data: dict, message: str, success: bool) -> dict:
    return {
        'message': message,
        'success': success,
        'min_temperature': temperature_data['min_temp'],
        'max_temperature': temperature_data['max_temp'],
        'temperature': temperature_data['temp'],
        'hour': datetime.now().day,
        'date': str(date.today())
    }
