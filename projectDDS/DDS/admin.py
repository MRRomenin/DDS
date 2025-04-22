from django.contrib import admin
from .models import Status, Type, Category, Subcategory, Transaction

class ProductAdmin(admin.ModelAdmin):
    list_display = ('status','type','category','date', 'subcategory', 'amount', 'comment')


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transaction, ProductAdmin)
# Register your models here.
