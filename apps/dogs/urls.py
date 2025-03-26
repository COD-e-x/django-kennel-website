from django.urls import path
from .apps import DogsConfig
from . import views

app_name = DogsConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("breeds/", views.breeds_list, name="breeds"),
    path("breeds/<int:pk>/dogs/", views.dogs_by_breed, name="dogs_by_breed"),
    path("dogs/", views.dogs_list, name="dogs_list"),
    path("dogs/create/", views.dog_create, name="dog_create"),
]
