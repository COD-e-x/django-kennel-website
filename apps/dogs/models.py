from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import NULLABLE
from apps.users.models import NULLABLE_FOR_STRING


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Порода"),
    )
    description = models.CharField(
        max_length=1000,
        verbose_name=_("Описание"),
        **NULLABLE_FOR_STRING,
    )
    photo = models.ImageField(
        upload_to="breed/",
        **NULLABLE,
        verbose_name=_("Фото"),
    )

    class Meta:
        verbose_name = _("Порода собаки")
        verbose_name_plural = _("Породы собак")

    def __str__(self):
        return f"{self.name}"


class Dog(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("Имя"),
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        verbose_name=_("Порода"),
    )
    photo = models.ImageField(
        upload_to="dogs/",
        **NULLABLE,
        verbose_name=_("Фото"),
    )
    birth_date = models.DateTimeField(
        **NULLABLE,
        verbose_name=_("Дата рождения"),
    )

    class Meta:
        verbose_name = _("Собака")
        verbose_name_plural = _("Собаки")

    def __str__(self):
        return f"{self.name} ({self.breed})"
