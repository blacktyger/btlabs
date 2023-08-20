from decimal import Decimal

import requests
from django.db import models

from core.utils import prices


class FundingWalletBalance(models.Model):
    timestamp = models.DateTimeField(editable=True)
    balances = models.JSONField(default=dict, null=True, blank=True)
    pending_transactions = models.IntegerField(default=0, null=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return f"Balance [{self.timestamp.strftime('%d-%m-%Y %H:%M')}]"


class FundingWalletTransaction(models.Model):
    timestamp = models.DateTimeField(editable=True)
    amount = models.DecimalField(default=0, null=True, max_digits=16, decimal_places=8)
    method = models.CharField(max_length=10, blank=True, null=True)
    chain = models.CharField(max_length=10, blank=True, null=True)
    coin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ('timestamp',)

    @property
    def usd_value(self):
        try:
            if self.coin.lower() == "epic":
                return self.amount * Decimal(prices())
            else:
                Decimal('0')

        except Exception as e:
            print(e)
            return self.amount

    def __str__(self):
        return f"Transaction [{self.timestamp.strftime('%d-%m-%Y %H:%M')}]"