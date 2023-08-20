from _decimal import Decimal
import json

import requests


def prices():
    try:
        BASE_URL = "https://api.coingecko.com/api/v3"
        url = f"{BASE_URL}/simple/price?ids=epic-cash&vs_currencies=usd"
        data = json.loads(requests.get(url).content)
        return Decimal(data['epic-cash']['usd'])
    except json.JSONDecodeError as er:
        print(er)
        return Decimal('0')


def received_in_percent(amount, goal):
    return round(amount / float(goal) * 100, 1)
