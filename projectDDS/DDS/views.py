from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SerializersTransaction
from django.http import JsonResponse
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


def get_subcategories(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id)
    subcategories_data = list(subcategories.values('id', 'name_subcategory'))

    return JsonResponse(subcategories_data, safe=False)

def delete(request, id):
    try:
        transact = Transaction.objects.get(id=id)
        transact.delete()
        return redirect('/DDS/')
    except Transaction.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def edit(request, id):
    # Получаем транзакцию по ID
    transaction = get_object_or_404(Transaction, id=id)

    # Если запрос POST, обрабатываем форму
    if request.method == 'POST':
        status = request.POST.get('status')
        transaction_type = request.POST.get('type')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        amount = request.POST.get('amount')
        comment = request.POST.get('comments')

        # Обновляем транзакцию
        transaction.status_id = status
        transaction.type_id = transaction_type
        transaction.category_id = category
        transaction.subcategory_id = subcategory
        transaction.amount = amount
        transaction.comment = comment
        transaction.save()

        return redirect('/DDS/')  # После редактирования, перенаправляем на главную страницу

    else:
        # Для GET-запроса передаем транзакцию в форму для редактирования
        status = Status.objects.all()
        type = Type.objects.all()
        category = Category.objects.all()
        subcategory = Subcategory.objects.filter(
            category=transaction.category)  # Фильтруем подкатегории по выбранной категории

        return render(request, 'edit.html', {
            'transaction': transaction,
            'status': status,
            'type': type,
            'category': category,
            'subcategory': subcategory
        })


class AuthorDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('author-list')

# def manager(request):
#     return render(request, 'manager.html')

def manager(request):
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    # Извлекаем все статусы из базы данных
    return render(request, "manager.html", {"statuses": statuses, "types": types,
                                            "categories": categories, "subcategories": subcategories})

def manager_add(request):
    if request.method == "POST":
        name = request.POST.get("name_status")
        if name:
            Status.objects.create(name_status=name)
    return redirect("manager")  # Название URL маршрута

def manager_delete(request, id):
    status = get_object_or_404(Status, id=id)
    status.delete()
    return redirect("manager")



def manager_add_type(request):
    if request.method == "POST":
        name_type = request.POST.get("name_type")
        if name_type:
            Type.objects.create(name_type=name_type)
    return redirect("manager")  # Название URL маршрута

def manager_delete_type(request, id):
    type_instance = get_object_or_404(Type, id=id)
    type_instance.delete()
    return redirect("manager")


def manager_add_category(request):
    if request.method == "POST":
        name_category = request.POST.get("name_category")
        if name_category:
            Category.objects.create(name_category=name_category)
    return redirect("manager")  # Название URL маршрута

def manager_delete_category(request, id):
    category_instance = get_object_or_404(Category, id=id)
    category_instance.delete()
    return redirect("manager")


def manager_add_subcategory(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')  # ID выбранной категории
        name_subcategory = request.POST.get('name_subcategory')  # Название подкатегории
        category = get_object_or_404(Category, id=category_id)  # Получаем категорию по ID
        if name_subcategory:
            Subcategory.objects.create(category=category, name_subcategory=name_subcategory)  # Создаём подкатегорию
        return redirect('manager')

def manager_delete_subcategory(request, id):
    subcategory_instance = get_object_or_404(Subcategory, id=id)
    subcategory_instance.delete()
    return redirect("manager")

# Create your views here.
