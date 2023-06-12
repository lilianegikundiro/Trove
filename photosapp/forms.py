from django import forms
from .models import photos

class UploadForm(forms.ModelForm):
    class Meta:
        model = photos
        fields = ['title', 'media']
