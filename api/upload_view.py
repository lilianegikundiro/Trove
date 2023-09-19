from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Image
from .serializers import ImageSerializer
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
    
