from django.db import models
from django.utils.timezone import now

# Create your models here.

from cloudinary.models import CloudinaryField

class photos(models.Model):
   
    
    title = models.CharField(max_length=100)
    media = CloudinaryField(resource_type='auto')
    date= models.DateTimeField(default=now)
 