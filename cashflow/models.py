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


class SubCategories(models.Model):
    subcategories = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subcategories}"


class Categories(models.Model):
    subcategories = models.ForeignKey('SubCategories', on_delete=models.RESTRICT, null=True)
    categories = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.categories}, {self.subcategories}"
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=255, verbose_name="Название")
    date = models.ForeignKey('Date', on_delete=models.RESTRICT, null=True)
    status = models.ForeignKey('Status', on_delete=models.RESTRICT, null=True)
    type = models.ForeignKey('Type', on_delete=models.RESTRICT, null=True)
    categories = models.ForeignKey('Categories', on_delete=models.RESTRICT, null=True)
    date = models.DateTimeField(default=timezone.now,
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(
        max_length=1000, help_text="Enter about transaction",
        null=True)

    def __str__(self):
        return f"{self.title}, {self.amount}"

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
