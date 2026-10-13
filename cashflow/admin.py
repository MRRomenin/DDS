from django.contrib import admin
from .models import Status, Type, Categories, SubCategories, Transaction

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Transaction)

# Register your models here.
