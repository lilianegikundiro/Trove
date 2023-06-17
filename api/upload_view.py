from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

import cloudinary
from cloudinary.uploader import upload
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PhotoSerializer
from cloudinary.models import CloudinaryResource

from photosapp.models import photos
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UploadViewSet(viewsets.ModelViewSet):
   
    # queryset = photos.objects.all()
    serializer_class = PhotoSerializer

    permission_classes = [IsAuthenticated]
 
    def create(self, request):
        image_file = request.FILES.get('image')
        if image_file:
            # Upload to Cloudinary
            upload_result = upload(image_file)
            image_url = upload_result.get('url')

            print(upload_result)
            # Save to the database
            title = request.data.get('title')
            photo = photos.objects.create(title=title, media=CloudinaryResource(upload_result),)
            serializer = self.get_serializer(photo)
            return Response(serializer.data)
        else:
            return Response({'error': 'No image file provided'}, status=400)




