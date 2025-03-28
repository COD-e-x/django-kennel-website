from django import forms
from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        widgets = {
            "birth_date": forms.DateInput(
                attrs={"placeholder": "ДД.ММ.ГГГГ", "class": "form-control"}
            ),
        }
