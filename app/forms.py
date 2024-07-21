from django import forms

class CityForm(forms.Form):
    city_name = forms.CharField(max_length=255, label="Enter city name")