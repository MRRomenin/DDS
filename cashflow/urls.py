from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_transaction, name='list'),
    path('delete/<uuid:part_id>/', views.delete_transaction, name='delete_part'),
]