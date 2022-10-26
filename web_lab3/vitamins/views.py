from rest_framework import viewsets
from vitamins.serializers import VitaminsSerializer
from vitamins.models import Vitamins


class VitaminsViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по цене
    queryset = Vitamins.objects.all().order_by('price')
    serializer_class = VitaminsSerializer # Сериализатор для модели