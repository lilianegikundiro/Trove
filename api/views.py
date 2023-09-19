from django.http import FileResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action

from urllib import response

# from .models import photos
from .serializers import UserSerializer, LoginSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# class IndexViewSet(viewsets.ModelViewSet):
# class IndexViewSet(viewsets.ModelViewSet):
#         queryset=photos.objects.all()
#         serializer_class=PhotoSerializer
        # return Response(serializer_class.data)
    

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    

class LoginViewSet(viewsets.ModelViewSet):
    
    serializer_class = LoginSerializer
    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        # user2 = User.objects.get(username=username)
        # token, created = Token.objects.get_or_create(user=user)
       
        
        if user is not None:
            login(request, user)
            
             # Delete existing token (if any)
            Token.objects.filter(user=user).delete()
            
            # Generate or retrieve the authentication token
            token, _ = Token.objects.get_or_create(user=user)
            
            serializer = self.get_serializer(user)
            return Response({"token":token.key})
        else:
            return Response({'error': 'Invalid username or password'}, status=400)

    def retrieve(self, request, pk=None):
        # Handle HTTP GET request to retrieve a specific user's information
        # You can customize the logic to fetch and return the user's data based on the provided 'pk'

        # Replace the following line with your own logic to retrieve the user's information
        user_data = {'username': 'example_user', 'email': 'example@example.com'}

        return Response(user_data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        # Handle HTTP PUT request to update a specific user's information
        # You can customize the logic to update the user's data based on the provided 'pk' and request data

        # Replace the following line with your own logic to update the user's information
        updated_user_data = {'username': 'updated_user', 'email': 'updated@example.com'}

        return Response(updated_user_data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        # Handle HTTP DELETE request to delete a specific user
        # You can customize the logic to delete the user based on the provided 'pk'

        # Replace the following line with your own logic to delete the user
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.http import HttpResponse

class FileDownloadViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def create(self, request):
        resource_url = request.query_params.get('resource_url')

        response = requests.get(resource_url)

        # Extract the file name from the URL
        file_name = resource_url.split("/")[-1]

        # Set the appropriate headers for file download
        file_response = HttpResponse(response.content, content_type='application/octet-stream')
        file_response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        file_response['Content-Length'] = len(response.content)

        return file_response

    


    