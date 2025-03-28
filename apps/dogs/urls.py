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
    path("dogs/create/<int:pk>/", views.dog_edit, name="dog_edit"),
    path("dogs/detail/<int:pk>/", views.dog_detail, name="dog_detail"),
    path("dogs/update/<int:pk>/", views.dog_update, name="dog_update"),
    path("dogs/delete/<int:pk>/", views.dog_delete, name="dog_create"),
    path("dogs/delete/<int:pk>/", views.dog_delete, name="dog_delete"),
]
