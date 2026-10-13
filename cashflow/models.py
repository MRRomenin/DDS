from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid


class Status(models.Model):
    name_status = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name_status


class Type(models.Model):
    type_operation = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.type_operation


class Categories(models.Model):
    categories = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.categories


class SubCategories(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    subcategories = models.CharField(max_length=100)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.subcategories


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=255, verbose_name="Enter about transaction")
    date = models.DateTimeField(default=timezone.now,
                                verbose_name='Дата и время')  # фиксация момента времени совершения транзакции
    status = models.ForeignKey('Status', on_delete=models.RESTRICT, verbose_name='Статус')
    operation_type = models.ForeignKey('Type', on_delete=models.RESTRICT, verbose_name='Тип')
    categories = models.ForeignKey('Categories', on_delete=models.RESTRICT, verbose_name='Категория')
    subcategories = models.ForeignKey('SubCategories', on_delete=models.RESTRICT, verbose_name='Подкатегория')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(
        max_length=1000, help_text="Enter about transaction",
        blank=True, verbose_name='Комментарий')

    def __str__(self):
        return (f"Transaction: {self.title}, date: {self.date}, status: {self.status}"
                f", type: {self.operation_type}, categories: {self.categories}, {self.amount}")

    def get_absolute_url(self):
        return reverse('transaction-details', args=[str(self.id)])

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ['-date']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(amount__gte=0),
                name='amount_gte_zero'
            )
        ]

# Create your models here.
