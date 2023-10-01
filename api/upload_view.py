from requests import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Image
from .serializers import ImageSerializer,EditImageSerializer,DeleteImageSerializer
from urllib import response
from rest_framework.decorators import action

class UploadImage(CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()
    
class ListImages(ListAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()
    
    def get_queryset(self):
        
        return Image.objects.filter(user=self.request.user)

class SingleImageView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    
    def get_queryset(self):
        # Customize the queryset to return only images/videos for the current user
        return Image.objects.filter(user=self.request.user)


class EditImageView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EditImageSerializer
    queryset = Image.objects.all()  # You can keep this queryset as it will be overridden in the `get_queryset` method

    def get_queryset(self):
        # Customize the queryset to return only images/videos for the current user
        return Image.objects.filter(user=self.request.user)
    
class DeleteImageView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = DeleteImageSerializer
    queryset = Image.objects.all()

    def delete(self, request, pk):
        try:
            image = Image.objects.get(pk=pk, user=request.user)
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist:
            return Response({"detail": "Image not found."}, status=status.HTTP_404_NOT_FOUND)