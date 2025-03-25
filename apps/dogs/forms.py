from django import forms

from apps.dogs.models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
