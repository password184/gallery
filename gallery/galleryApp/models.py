from django.db import models
import uuid
from galleryUser.models import About

# Create your models here.

class Gallery(models.Model):
    owner = models.ForeignKey(About, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    gallery_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
      return self.name
