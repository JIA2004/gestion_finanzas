import requests
from django.conf import settings

ALPHA_VANTAGE_API_KEY = settings.API_KEY
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'

def obtener_precio_actual(ticker):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': ticker,
        'apikey': ALPHA_VANTAGE_API_KEY,
    }
    response = requests.get(ALPHA_VANTAGE_URL, params=params)
    data = response.json()
    try:
        precio = float(data['Global Quote']['05. price'])
        return precio
    except (KeyError, ValueError):
        return None
