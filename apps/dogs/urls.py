from django.urls import path
from apps.dogs.views import (
    index,
    breeds_list,
    dogs_by_breed,
    dogs_list,
    dog_create,
)
from apps.dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("breeds/", breeds_list, name="breeds"),
    path("breeds/<int:pk>/dogs/", dogs_by_breed, name="dogs_by_breed"),
    path("dogs/", dogs_list, name="dogs_list"),
    path("dogs/create/", dog_create, name="dog_create"),
]
