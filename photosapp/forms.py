from django import forms
from .models import photos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadForm(forms.ModelForm):
    class Meta:
        model = photos
        fields = ['title', 'media']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
