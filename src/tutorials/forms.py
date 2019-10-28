from django import forms

from .models import Tutorial

class TutorialForm(forms.ModelForm):
    title = forms.CharField(max_length=128, min_length=2, strip=True, widget=forms.TextInput(
        attrs={'class ': 'form-control rounded-0 '}))
    content = forms.CharField(widget=forms.Textarea({'class': 'form-control rounded-0'}))

    class Meta:
        model = Tutorial
        fields = ['title', 'content']