from django.contrib import admin
from .models import Status, Type, Categories, SubCategories, Transaction


class SubcategoriesInline(admin.TabularInline):
    model = SubCategories
    extra = 0


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status'
                        , 'operation_type', 'categories', 'subcategories', 'amount', 'comment')

    fields = ['title', 'date', 'status', 'operation_type',  ('categories', 'subcategories'),
              'amount', 'comment']

    list_filter = ('date',) # fix it


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name_status',)

    fields = ['name_status']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_operation',)

    fields = ['type_operation']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories',)

    fields = ['categories']

    inlines = [SubcategoriesInline]

@admin.register(SubCategories)
class SubCategories(admin.ModelAdmin):
    list_display = ('category', 'subcategories')

    fields = ['category', 'subcategories']



# Register your models here.
