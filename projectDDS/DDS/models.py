from django.db import models
import datetime

"""В ORM представлено несколько моделей: такие как Status, Type, Category, SubCategory и Transaction. 
    Все модели имеют внешний ключ у Transaction. Модель Date не был реализован."""


class Status(models.Model):
    name_status = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name_status

class Type(models.Model):
    name_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name_type

class Category(models.Model):
    name_category = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name_category

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_subcategory = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name_subcategory

class Transaction(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    date = models.DateTimeField(auto_now_add=True,  null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Подкатегория')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    objects = models.Manager()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return (f"Transaction {self.id} - {self.status} - {self.amount} руб. - {self.category} - "
                f"{self.subcategory} - {self.date} ")


# Create your models here.
