from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from currency.models import CurrencyHistory
from currency.repository import get_history
from currency.service import get_exchange_rate


def create_response(history):
    rub_pair = get_exchange_rate()
    CurrencyHistory.objects.create(usd=rub_pair["value"])

    response_data = {
        'success': True,
        'current_usd': rub_pair["value"],
        'history': history
    }

    return JsonResponse(response_data)


def get_current_usd(request):
    history = get_history()

    if history:
        last_created_at = history[-1]["created_at"]
        time_difference = timezone.now() - timedelta(seconds=10)

        if last_created_at < time_difference:
            return create_response(history)

        return JsonResponse({
            "success": False,
            "detail": "You can request the exchange rate once every 10 seconds"
        })

    return create_response(history)
