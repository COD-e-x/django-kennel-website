from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.dogs.models import Breed, Dog
from apps.dogs.forms import DogForm


def index(request):
    """Отображает главную страницу с перечнем первых 3-х пород."""
    context = {
        "breeds": Breed.objects.all()[:3],
        "title": "Питомник - Главная",
    }
    return render(
        request,
        "dogs/index.html",
        context,
    )


def breeds_list(request):
    """Отображает список всех пород собак."""
    context = {
        "breeds": Breed.objects.all(),
        "title": "Питомник - Все наши породы",
    }
    return render(
        request,
        "dogs/breed/list.html",
        context,
    )


def dogs_by_breed(request, pk: int):
    """Отображает список собак для конкретной породы."""
    breed = get_object_or_404(Breed, pk=pk)
    context = {
        "dogs": Dog.objects.filter(breed_id=pk),
        "title": f"Собаки породы - {breed.name}",
        "breed_pk": breed.pk,
    }
    return render(
        request,
        "dogs/dog/list.html",
        context,
    )


def dogs_list(request):
    """Отображает список всех собак в питомнике."""
    context = {
        "dogs": Dog.objects.all(),
        "title": "Питомник - Все наши собаки",
    }
    return render(
        request,
        "dogs/dog/list.html",
        context,
    )


def dog_create(request):
    """
    Обрабатывает создание новой собаки через форму.
    Если форма валидна, сохраняет собаку и перенаправляет на список собак.
    """
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dogs:dogs_list"))
    return render(
        request,
        "dogs/dog/create.html",
        {"form": DogForm()},
    )
