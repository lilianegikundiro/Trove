from django.urls import path
from photosapp import views
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('', views.LoginView.as_view(),name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('index/<pk>/delete', views.IndexView.as_view, name='delete_photo'),
    path('pic/<pk>/delete', views.PhotoDeleteView.as_view(), name='delete'),
    
    

]