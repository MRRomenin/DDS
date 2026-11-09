from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_transaction, name='list'),
    path('delete/<uuid:part_id>/', views.list_transaction, name='delete_part'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('directory/', views.display_directory, name='directory'),
    path('delete/<slug:directory>/', views.delete_directory, name='delete_mass'),
    path('edit/<uuid:part_id>/', views.edit_transaction, name='edit_part'),
    path('add_directory/<slug:method_object>/', views.add_directory, name='add_directory'),
]