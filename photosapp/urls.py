from django.urls import path
from photosapp import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    

]