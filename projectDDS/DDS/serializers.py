# from django.db import models
from rest_framework import serializers
from .models import Transaction

class SerializersTransaction(serializers.ModelSerializer):
    class Meta:
        model = Transaction  # Указываем модель, с которой работает сериализатор
        fields = '__all__'  # Сериализуем все поля модели
