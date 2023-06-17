from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from urllib import response

from photosapp.models import photos
from .serializers import PhotoSerializer, UserSerializer, LoginSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UploadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset=photos.objects.all()
    # serializer_class=PhotoSerializer
    @action(methods=['post'], detail=False)
    def upload(self, request):
        return Response({"messsage":"Upload check"})