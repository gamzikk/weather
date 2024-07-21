from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

class WeatherForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)