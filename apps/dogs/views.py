from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Breed, Dog
from .forms import DogForm


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
    """Обрабатывает создание новой собаки через форму."""
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dogs:dogs_list")
    else:
        form = DogForm()
    return render(
        request,
        "dogs/dog/create.html",
        {"form": form, "dog": None},
    )


def dog_edit(request, dog_id):
    """Обрабатывает редактирование собаки через форму."""
    dog = get_object_or_404(Dog, id=dog_id)
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return redirect("dogs:dogs_list")
    else:
        form = DogForm(instance=dog)
    return render(
        request,
        "dogs/dog/create.html",
        {"form": form, "dog": dog},
    )
