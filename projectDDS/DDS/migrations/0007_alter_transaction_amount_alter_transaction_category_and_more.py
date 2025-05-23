# Generated by Django 5.2 on 2025-04-23 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDS', '0006_rename_name_status_name_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DDS.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DDS.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DDS.subcategory', verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DDS.type', verbose_name='Тип'),
        ),
    ]
