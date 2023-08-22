from django.shortcuts import render


def home(request):
    context = {
        # 'received_percent': received_in_percent(goal=5000),
        'milestone_goal': '1 000',
        'project_title': 'Epic Easy Miner',
        # 'total_payments': total_payments(),
        # 'last_update': FundingWalletBalance.objects.last().timestamp,
        # 'history': transaction_history(),
        # 'total': total_received_funds_in_usd()  # rounded in USD
        }

    html_template = 'easyminer/home.html'
    return render(request, html_template, context)





