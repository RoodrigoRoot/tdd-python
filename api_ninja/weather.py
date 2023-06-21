import requests

def send_request_temperature(city: str, country: str) -> dict:
    try:
        api_url = f'https://api.api-ninjas.com/v1/weather?city={city}&country={country}'
        response = requests.get(api_url, headers={'X-Api-Key': 'Cp91WT2Iz2OtvNhFI8x/RQ==BNy1ErAMZmjeVWpq'})
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}
