from _decimal import Decimal

import requests

from apps.funding.models import FundingWalletTransaction


def prices():
    try:
        url = 'https://epic-radar.com/api/coingecko/'
        response = requests.get(url=url)

        if response.status_code == 200:
            return response.json()['results'][0]
    except Exception as e:
        print(e)
        return


def total_payments():
    return FundingWalletTransaction.objects.count()

def received_in_percent(amount, goal):
    return round(amount / float(goal) * 100, 1)


def total_received_in_percent(goal):
    return round(total_received_funds_in_usd() / float(goal) * 100, 1)


def total_received_funds_in_usd():
    amount = balance_from_transactions() * Decimal(prices()[f'epic_vs_usd'])
    return int(amount)


def transaction_history():
    return FundingWalletTransaction.objects.filter(amount__gt=0.9).order_by('-timestamp')


def balance_from_transactions():
    txs = transaction_history()
    return Decimal(sum([tx.amount for tx in txs]))