from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Image
from .serializers import ImageSerializer


class UploadImage(CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()
