"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *
from .upload_view import ListImages, UploadImage, SingleImageView,EditImageView, DeleteImageView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationViewSet

router=routers.DefaultRouter()
# router.register(r'media/download', FileDownloadViewSet, basename='file-download')

urlpatterns = [
     path('register/', RegistrationViewSet.as_view({'get': 'list', 'post': 'create'}), name='apiRegistration'),
     path('login/',LoginViewSet.as_view({'get': 'list','post': 'login', 'put': 'update', 'delete': 'destroy'}),name='apiLogin'),
     path("",include(router.urls)),
     path("media/upload/", UploadImage.as_view()),
     path("media/list/", ListImages.as_view()),
       path('media/<int:pk>/delete/', DeleteImageView.as_view()),
     path('media/<int:pk>/', SingleImageView.as_view()),
     path('media/<int:pk>/edit/', EditImageView.as_view()),
   
     path("media/download/",FileDownloadViewSet.as_view({'get': 'create'}))
]
