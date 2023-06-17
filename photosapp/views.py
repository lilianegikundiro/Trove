from telnetlib import LOGOUT
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import photos
from .forms import UploadForm
import cloudinary
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'photosapp/registration.html'
    success_url = reverse_lazy('login')



# Create your views here.


class IndexView(LoginRequiredMixin,View):
    def get(self, request):
        photo = photos.objects.all()
        ctx = {'photo':photo}
        return render(request, 'photosapp/index.html', ctx)





class UploadView(LoginRequiredMixin,View):
    def get(self, request):
        form = UploadForm()
        return render(request, 'photosapp/upload.html', {'form': form})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'index' with the appropriate URL or view name
        return render(request, 'photosapp/upload.html', {'form': form})






    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'photosapp/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'index' with the appropriate URL or view name
            else:
                form.add_error(None, 'Invalid login credentials')
        return render(request, 'photosapp/login.html', {'form': form})
    
def LogoutUser(request):
	logout(request)
	return redirect('login')

#Exceptions
def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>ERROR 404</h1><br><p>Page Not Found</p>')
