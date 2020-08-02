from django import forms
from .models import team

class TeamForm(forms.ModelForm):
    class Meta:
        model = team
        fields =  ('name', 'size', 'university', 'boarding')