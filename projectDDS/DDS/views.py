from django.shortcuts import render

# from django.http import HttpResponse


def index(request):
    return render(request, '../templates/index.html')

def create_entry(request):
    return render(request, 'create_entry.html')

# Create your views here.
