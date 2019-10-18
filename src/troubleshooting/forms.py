from django import forms
from mdeditor.fields import MDTextFormField

from .models import Problem

class ProblemForm(forms.ModelForm):
    name = forms.CharField(max_length=128, min_length=2, strip=True, widget=forms.TextInput(
        attrs={'class ': 'form-control rounded-pill '}))
    description = MDTextFormField()

    class Meta:
        model = Problem
        fields = [
            'name',
            'description',
        ]