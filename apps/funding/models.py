from decimal import Decimal

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
    usd = models.DecimalField(default=0, null=True, max_digits=16, decimal_places=2)

    class Meta:
        ordering = ('timestamp',)

    def save(self, *args, **kwargs):
        if self.coin.lower() == "epic":
            self.usd = self.usd_value()

        super(FundingWalletTransaction, self).save(*args, **kwargs)

    def usd_value(self):
        try:
            if self.coin.lower() == "epic":
                return self.amount * Decimal(prices())
            else:
                Decimal('0')

        except Exception as e:
            print(e)
            return self.amount

    @classmethod
    def total_received_in_percent(cls, goal):
        return round(float(cls.balance_from_transactions_usd()) / float(goal) * 100, 1)

    @classmethod
    def transaction_history(cls):
        return cls.objects.filter(amount__gt=0.9).order_by('-timestamp')

    @classmethod
    def total_payments(cls):
        return cls.objects.count()

    @classmethod
    def balance_from_transactions_usd(cls):
        txs = cls.transaction_history()
        return Decimal(sum([tx.usd for tx in txs]))

    def __str__(self):
        return f"Transaction [{self.timestamp.strftime('%d-%m-%Y %H:%M')}]"