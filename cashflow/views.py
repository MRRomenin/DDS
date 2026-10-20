from django.shortcuts import render
from .models import Status, Type, Categories, SubCategories, Transaction
import requests
import xmltodict

CB_URL = "http://www.cbr.ru/scripts/XML_daily.asp"


def search_valute(valute: str, data: dict) -> str:
    target_dict = next((d for d in data if d.get('Name') == valute), None)
    if target_dict is None:
        return f"{valute}: валюта не найдена"

    return f"{valute}: {target_dict['Value']}"


def get_valute() -> dict | str:
    try:
        response = requests.get(CB_URL, timeout=10)
        response.raise_for_status()
        data = xmltodict.parse(response.content)
        rub_rate = data['ValCurs']['Valute']

        return {
            "dollar": search_valute('Доллар США', rub_rate),
            "euro": search_valute('Евро', rub_rate),
            "yuan": search_valute('Юань', rub_rate)
        }

    except (requests.RequestException, KeyError) as e:
        return {"error": "Не удалось получить курсы валют"}


def list_transaction(request):
    transact = Transaction.objects.all()

    context = {
        'transacts': transact,
        **get_valute(),
    }

    return render(request, 'transaction/list.html', context=context)
