from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_transaction, name='list'),
]