# room/forms.py

from django import forms
from core.forms import SignUpForm
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']
