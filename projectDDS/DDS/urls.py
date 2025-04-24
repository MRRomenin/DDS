from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.create_entry, name='create_entry'),
    path('manager/', views.manager, name='manager'),
    path("delete/<int:id>/", views.delete, name='delete'),
    path("edit/<int:id>/", views.edit, name='edit'),

    path('add/', views.manager_add, name='manager_add'),
    path('delete_manage/<int:id>/', views.manager_delete, name='manager_delete'),

    path('add_type/', views.manager_add_type, name='manager_add_type'),
    path('delete_manage_type/<int:id>/', views.manager_delete_type, name='manager_delete_type'),

    path('add_category/', views.manager_add_category, name='manager_add_category'),
    path('delete_manage_category/<int:id>/', views.manager_delete_category, name='manager_delete_category'),

    path('add_subcategory/', views.manager_add_subcategory, name='manager_add_subcategory'),
    path('delete_manage_subcategory/<int:id>/', views.manager_delete_subcategory, name='manager_delete_subcategory'),
]