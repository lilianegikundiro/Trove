from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Image(models.Model):

    media = CloudinaryField(resource_type='auto')
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/dbgooph5c/{self.media}"
        )

 