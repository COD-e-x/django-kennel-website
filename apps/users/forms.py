from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput, min_length=8
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        """Валидация пароля."""
        cd = self.cleaned_data
        password1 = cd.get("password")
        password2 = cd.get("password2")
        if password1 != password2:
            raise ValidationError("Пароли не совпадают!")
        return password2

    def clean_email(self):
        """Валидация email"""
        email = self.cleaned_data.get("email").strip().lower()
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Некорректный email!")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже зарегистрирован!")
        return email
