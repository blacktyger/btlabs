from django.shortcuts import render

from apps.funding.models import FundingWalletBalance
from core.utils import received_in_percent, total_received_funds_in_usd, total_payments, transaction_history


def home(request):
    total = total_received_funds_in_usd()
    context = {
        'total': total,  # rounded in USD
        # 'received_percent': received_in_percent(goal=7000),
        'total_received': 500,
        'milestone_giver': total,
        'milestone_giver_goal': 1000,
        'milestone_giver_in_percent': received_in_percent(total, 1000),
        'milestone_tipbot': 1,
        'milestone_tipbot_goal': 2000,
        'milestone_tipbot_in_percent': received_in_percent(1, 2000),
        'milestone_epicweb': 100,
        'milestone_epicweb_goal': 4000,
        'milestone_epicweb_in_percent': received_in_percent(1, 4000),
        # 'milestone_goal': '1 000',
        'project_title': 'Projects',
        'total_payments': total_payments(),
        'last_update': FundingWalletBalance.objects.last().timestamp,
        'history': transaction_history(),
        }

    html_template = 'projects/home.html'
    return render(request, html_template, context)





