from django.shortcuts import render, redirect, get_object_or_404
from .models import Status, Type, Categories, SubCategories, Transaction
from django.core.cache import cache
import requests
import xmltodict
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from .forms import FormTransaction


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


def list_transaction(request, part_id=None):
    if request.method == 'POST':
        delete_transaction(Transaction.objects.get(id=part_id))
        return redirect('list')

    transact = Transaction.objects.all()
    context = {
        'transacts': transact,
        'rates': get_valute(),
    }
    return render(request, 'transaction/list.html', context=context)


def delete_transaction(response_object: Transaction):
    response_object.delete()

def edit_transaction(request, part_id=None):
    post = get_object_or_404(Transaction, pk=part_id)
    if request.method == 'POST':
        form = FormTransaction(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = FormTransaction(instance=post)

    context = {
        'form': form,
        'title': "Редактирование транзакции",
        'text_button': "Редактировать",

    }

    return render(request, 'transaction/from_transact.html', context=context)


def add_transaction(request):
    if request.method == 'POST':
        form = FormTransaction(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = FormTransaction()

    context = {
        'form': form,
        'title': "Добавление транзакции",
        'text_button': "Отправить",
    }

    return render(request, 'transaction/from_transact.html', context=context)
