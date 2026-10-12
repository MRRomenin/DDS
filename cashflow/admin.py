from django.contrib import admin
from .models import Date, Status, Type, SubCategories, Categories, Transaction

admin.site.register(Date)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(SubCategories)
admin.site.register(Categories)
admin.site.register(Transaction)


# Register your models here.
