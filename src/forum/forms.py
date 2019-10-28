from django import forms

from .models import Thread

class ThreadForm(forms.ModelForm):
    subject = forms.CharField(max_length=128, min_length=2, strip=True, widget=forms.TextInput(
        attrs={'class ': 'form-control rounded-0'}))
    body = forms.CharField(widget=forms.Textarea({'class': 'form-control rounded-0'}))

    class Meta:
        model = Thread
        fields = [
            'subject',
            'body',
        ]