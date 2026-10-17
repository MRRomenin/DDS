from django.shortcuts import render
from .models import Status, Type, Categories, SubCategories, Transaction

# Create your views here.
def list_transaction(request):
    transact = Transaction.objects.all()

    context = {
        'transacts': transact,
    }

    return render(request, 'transaction/list.html', context=context)