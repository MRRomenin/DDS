# Generated by Django 5.2 on 2025-04-22 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DDS', '0005_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='name',
            new_name='name_status',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='name_subcategory',
        ),
    ]
