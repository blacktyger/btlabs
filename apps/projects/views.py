from django.shortcuts import render

from apps.funding.models import FundingWalletBalance, FundingWalletTransaction
from core.utils import received_in_percent


def home(request):
    tx_model = FundingWalletTransaction
    total = float(tx_model.balance_from_transactions_usd())

    context = {
        'total': total,  # rounded in USD
        'milestone_giver': '1080',
        'milestone_giver_goal': 1000,
        'milestone_giver_in_percent': received_in_percent(1080, 1000),
        'milestone_tipbot': 2000,
        'milestone_tipbot_goal': 2000,
        'milestone_tipbot_in_percent': received_in_percent(2000, 2000),
        'milestone_epicweb': 100,
        'milestone_epicweb_goal': 4000,
        'milestone_epicweb_in_percent': received_in_percent(1, 4000),
        'project_title': 'Projects',
        'total_payments': tx_model.total_payments(),
        'last_update': FundingWalletBalance.objects.last().timestamp,
        'history': tx_model.transaction_history(),
        }

    html_template = 'projects/home.html'
    return render(request, html_template, context)





