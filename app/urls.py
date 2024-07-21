from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("history/", views.history, name="history"),
    path("api/history/", views.api_history, name="api_history"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]