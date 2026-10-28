from django.shortcuts import render, redirect
from .models import Status, Type, Categories, SubCategories, Transaction
from django.core.cache import cache
import requests
import xmltodict
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
import logging
from django.shortcuts import get_object_or_404

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


def transaction_objects():
    status_object = Status.objects.all()
    type_object = Type.objects.all()
    category_object = Categories.objects.all()
    subcategory_object = SubCategories.objects.all()
    context = {
        'status_object': status_object,
        'type_objects': type_object,
        'category_object': category_object,
        'subcategory_object': subcategory_object,
    }

    return context


def add_transaction(request):
    if request.method == 'POST':
        status = get_object_or_404(Status, pk=request.POST.get('status_object'))
        operation_type = get_object_or_404(Type, pk=request.POST.get('type_object'))
        categories = get_object_or_404(Categories, pk=request.POST.get('category_object'))
        subcategories = get_object_or_404(SubCategories, pk=request.POST.get('subcategory_object'))
        error = None
        amount = None

        try:
            amount = Decimal(request.POST.get('amount', '').strip().replace(',', '.'))

        except InvalidOperation:
            error = 'Введите число'

        if error is None and not (amount.is_finite() and amount > 0):
            error = 'Сумма должна быть больше нуля'

        if error:
            context = transaction_objects()
            context['error'] = error
            return render(request, 'transaction/from_transact.html', context=context)

        result = Transaction.objects.create(title=request.POST.get('name_transaction'), status=status,
                                   operation_type=operation_type, categories=categories,
                                   subcategories=subcategories, amount=amount,
                                   comment=request.POST.get('comment'))

        return redirect('list')

    return render(request, 'transaction/from_transact.html', context=transaction_objects())
