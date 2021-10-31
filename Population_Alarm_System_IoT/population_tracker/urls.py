from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("sensor_data_delete/delete/<int:pk>", views.sensor_data_delete, name="sensor_data_delete")
]
