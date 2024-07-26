from django.urls import path
from .views import calculate_distance

urlpatterns = [
    path('distance/', calculate_distance, name='calculate_distance'),
]