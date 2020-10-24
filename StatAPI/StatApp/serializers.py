from rest_framework import serializers
from .models import StatModel


class StatSerializer(serializers.ModelSerializer):
    "Класс для приведения Джанго модели в JSON и обратно"

    class Meta:
        model = StatModel
        fields = '__all__'
