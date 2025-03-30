from django.urls import path

from .apps import UsersConfig
from . import views


app_name = UsersConfig.name


urlpatterns = [
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
]
