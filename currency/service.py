import requests
from django.conf import settings


def get_exchange_rate():
    url = f"https://api.currencyapi.com/v3/latest?apikey={settings.API_KEY}"

    response = requests.get(url)
    response_json = response.json()
    rub_pair = response_json['data']['RUB']

    return rub_pair
