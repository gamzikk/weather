from django.test import TestCase
from .models import City, WeatherForecast

class CityModelTest(TestCase):
    def test_city_creation(self):
        city = City(name="Test City")
        city.save()
        self.assertEqual(City.objects.count(), 1)

class WeatherForecastModelTest(TestCase):
    def test_weather_forecast_creation(self):
        city = City(name="Test City")
        city.save()
        weather_forecast = WeatherForecast(city=city, temperature=20.0, wind_speed=5.0)
        weather_forecast.save()
        self.assertEqual(WeatherForecast.objects.count(), 1)

class ViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_weather_forecast_view(self):
        city = City(name="Test City")
        city.save()
        response = self.client.post("/", {"city_name": city.name})
        self.assertEqual(response.status_code, 200)