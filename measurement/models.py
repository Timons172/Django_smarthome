from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название датчика')
    description = models.CharField(max_length=100, verbose_name='Описание датчика')

    def __str__(self):
        return self.name + self.description

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение')
