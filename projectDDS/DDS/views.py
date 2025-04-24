from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework import status
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SerializersTransaction

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# @api_view(['GET'])




# def getData(request):
#     if request.method == 'GET':
#         trans = Transaction.objects.all()
#         serializer = SerializersTransaction(trans, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SerializersTransaction(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = SerializersTransaction
#
# class TransactionListCreate(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = SerializersTransaction

# Представление для редактирования или удаления транзакции
# class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()    path("", views.index, name="index"),
#     path('create/', views.create_entry, name='create_entry'),
#     path('manager/', views.manager, name='manager'),
#     serializer_class = SerializersTransaction

def index(request):
    transact = Transaction.objects.all()
    return render(request, '../templates/index.html', locals())



def create_entry(request):
    # transact_create = Transaction.objects.all()

    if request.method == 'POST':

        # Получаем данные из формы
        status = request.POST.get('status')
        transaction_type = request.POST.get('type')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        amount = request.POST.get('amount')
        comment = request.POST.get('comments')

        print(f"Status: {status}, Type: {transaction_type}, Amount: {amount}, Comments: {comment}")
        # Создание новой транзакции
        new_transaction = Transaction(
            status_id=status,
            type_id=transaction_type,
            category_id=category,
            subcategory_id=subcategory,
            amount=amount,
            comment=comment
        )
        new_transaction.save()

        # После создания записи редиректим на другую страницу
        return redirect('/DDS/')  # Замените на URL, куда хотите перенаправить

    # В случае GET-запроса передаем все объекты для селектов
    transact_create = Transaction.objects.all()  # Тут нужно подставить правильные объекты для селектов

    status = Status.objects.all()
    type = Type.objects.all()
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    return render(request, 'create_entry.html', {'transact_create': transact_create, 'status': status,
        'type': type, 'category': category, 'subcategory': subcategory})

def delete(request, id):
    try:
        transact = Transaction.objects.get(id=id)
        transact.delete()
        return redirect('/DDS/')
    except Transaction.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

class AuthorDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('author-list')

def manager(request):
    return render(request, 'manager.html')




# def add_transaction(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction-list')  # Перенаправляем на страницу со списком транзакций
#     else:
#         form = TransactionForm()
#     return render(request, 'add_transaction.html', {'form': form})
#
# def transaction_list(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'transaction_list.html', {'transactions': transactions})

# Create your views here.
