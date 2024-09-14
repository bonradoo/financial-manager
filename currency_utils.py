# currency_utils.py

import requests
import os
import json
import base64
from cryptography.fernet import Fernet, InvalidToken

# Cache directory
CACHE_DIR = os.path.join(os.path.dirname(__file__), 'data', 'cache')
os.makedirs(CACHE_DIR, exist_ok=True)

def get_exchange_rate(api_key, base_currency, target_currency):
    # Check if rate is cached
    cache_file = os.path.join(CACHE_DIR, f'{base_currency}_{target_currency}.json')
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            data = json.load(f)
            timestamp = data.get('timestamp')
            # Check if cached data is from today
            if timestamp == get_current_date():
                return data.get('rate')

    # Fetch exchange rate from API
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['result'] == 'success':
            rate = result['conversion_rate']

            # Cache the rate
            data = {
                'rate': rate,
                'timestamp': get_current_date(),
            }
            with open(cache_file, 'w') as f:
                json.dump(data, f)

            return rate
        else:
            return None
    else:
        return None

def get_currency_list(api_key):
    # Cache per API key to prevent conflicts
    cache_file = os.path.join(CACHE_DIR, f'currency_list_{api_key}.json')
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            data = json.load(f)
            return data

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/codes'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['result'] == 'success':
            currency_list = {code: name for code, name in result['supported_codes']}

            # Cache the currency list
            with open(cache_file, 'w') as f:
                json.dump(currency_list, f)

            return currency_list
        else:
            return None
    else:
        return None


def get_current_date():
    from datetime import datetime
    return datetime.utcnow().strftime('%Y-%m-%d')
