from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_transaction, name='list'),
    path('delete/<uuid:part_id>/', views.list_transaction, name='delete_part'),
    path('add/', views.add_transaction, name='add_transaction')
]