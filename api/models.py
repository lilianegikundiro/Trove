from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User  


class Image(models.Model):

    media = CloudinaryField(resource_type='auto')
    timestamp = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/dbgooph5c/{self.media}"
        )

 