from _decimal import Decimal
import json

import requests

from apps.funding.models import FundingWalletTransaction


def prices():
    try:
        BASE_URL = "https://api.coingecko.com/api/v3"
        url = f"{BASE_URL}/simple/price?ids=epic-cash&vs_currencies=usd"
        data = json.loads(requests.get(url).content)
        return Decimal(data['epic-cash']['usd'])
    except json.JSONDecodeError as er:
        print(er)
        return Decimal('0')


def total_payments():
    return FundingWalletTransaction.objects.count()


def received_in_percent(amount, goal):
    return round(amount / float(goal) * 100, 1)


def total_received_in_percent(goal):
    return round(total_received_funds_in_usd() / float(goal) * 100, 1)


def total_received_funds_in_usd():
    amount = balance_from_transactions() * prices()
    return int(amount)


def transaction_history():
    return FundingWalletTransaction.objects.filter(amount__gt=0.9).order_by('-timestamp')


def balance_from_transactions():
    txs = transaction_history()
    return Decimal(sum([tx.amount for tx in txs]))