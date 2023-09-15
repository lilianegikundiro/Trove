from django.db import models
from django.utils.timezone import now
# from django.contrib.auth.models import User  

# Create your models here.

from cloudinary.models import CloudinaryField

class photos(models.Model):
   
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    media = CloudinaryField(resource_type='auto')
    date= models.DateTimeField(default=now)
 