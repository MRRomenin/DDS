from django.shortcuts import render

from .models import Transaction

# from django.http import HttpResponse


def index(request):
    transact = Transaction.objects.all()
    return render(request, '../templates/index.html', locals())

def create_entry(request):
    return render(request, 'create_entry.html')

def manager(request):
    return render(request, 'manager.html')


# Create your views here.
