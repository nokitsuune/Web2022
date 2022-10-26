from vitamins.models import Vitamins
from rest_framework import serializers


class VitaminsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Vitamins
        # Поля, которые мы сериализуем
        fields = ["pk", "title", "description", "price"]