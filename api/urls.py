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
from .upload_view import UploadViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationViewSet

router=routers.DefaultRouter()
router.register(r"upload",UploadViewSet,basename="upload")

urlpatterns = [
     path('upload/', UploadViewSet.as_view({'post': 'upload'}),name="upload"),
     path('index/', IndexViewSet.as_view({'get': 'list', 'post': 'create'})),
     path('register/', RegistrationViewSet.as_view({'get': 'list', 'post': 'create'}), name='registration'),
     path('login/',LoginViewSet.as_view({'post': 'login', 'put': 'update', 'delete': 'destroy'}),name='login'),
     path("",include(router.urls)),
]