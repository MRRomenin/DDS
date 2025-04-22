from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.create_entry, name='create_entry'),
    path('manager/', views.manager, name='manager')
]