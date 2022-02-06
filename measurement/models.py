from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(decimal_places=2, max_digits=4)
    created_at = models.DateField(auto_now_add=True)
