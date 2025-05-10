from django import forms
from .models import Poet

class PoetForm(forms.ModelForm):
    class Meta:
        model = Poet
        fields = ['name', 'birth_date', 'death_date', 'biography', 'works']
