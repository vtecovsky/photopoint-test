from currency.models import CurrencyHistory


def get_history():
    """
    Получение 10 последних запросов курсов.
    :return: 10 последних запросов
    """

    history = CurrencyHistory.objects.all()[:10].values()
    return list(history)
