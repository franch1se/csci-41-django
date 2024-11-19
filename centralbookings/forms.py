from .models import *
from django import forms

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = organizer
        fields = ['organizer_name']