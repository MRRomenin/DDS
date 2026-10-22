from django.shortcuts import render, redirect
from .models import Status, Type, Categories, SubCategories, Transaction
from django.core.cache import cache
import requests
import xmltodict
from decimal import Decimal, ROUND_HALF_UP
import logging

CB_URL = "http://www.cbr.ru/scripts/XML_daily.asp"


def search_valute(valute: str, data: dict, symbol: str) -> dict | str:
    target_dict = next((d for d in data if d.get('Name') == valute), None)
    if target_dict is None:
        return f"{valute}: валюта не найдена"
    valute_decimal = Decimal(target_dict['Value'].replace(',', '.')).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    valute_info = {'name': valute, 'valute': valute_decimal, 'symbol': symbol}
    return valute_info


def get_valute() -> dict | str:
    rates = cache.get('cbr_rates')
    if rates is not None:
        return rates

    try:
        logger.info("Запрос к ЦБ")
        response = requests.get(CB_URL, timeout=10)
        response.raise_for_status()
        data = xmltodict.parse(response.content)
        rub_rate = data['ValCurs']['Valute']

        rates = {
            "dollar": search_valute('Доллар США', rub_rate, '$'),
            "euro": search_valute('Евро', rub_rate, '€'),
            "yuan": search_valute('Юань', rub_rate, '¥')
        }
        cache.set('cbr_rates', rates, 60 * 60)
        return rates

    except (requests.RequestException, KeyError) as e:
        return {"error": f"Не удалось получить курсы валют {e}"}


def list_transaction(request):
    transact = Transaction.objects.all()

    context = {
        'transacts': transact,
        'rates': get_valute(),
    }

    return render(request, 'transaction/list.html', context=context)

def delete_transaction(request, part_id=None):
    my_object = Transaction.objects.get(id=part_id)
    logger.info(f"[INFO] ID транзакции: {my_object.id}")
    my_object.delete()
    return redirect('list')
