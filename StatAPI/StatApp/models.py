from django.db import models
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.

class StatModel(models.Model):
    "Базовая модель для данных статистики"

    name = models.TextField()
    data = models.TextField()
    timestamp = UnixDateTimeField()

    def __str__(self):
        return self.name
