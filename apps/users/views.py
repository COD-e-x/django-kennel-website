from django.shortcuts import render, redirect, reverse

from .forms import UserRegisterForm


def user_register(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return redirect("dogs:index")

    context = {
        "title": "Создать аккаунт",
        "form": form,
    }
    return render(request, "users/register.html", context)
