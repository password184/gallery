from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField (blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile", default="profile/aaron-burden-xtIYGB0KEqc-unsplash.jpg")
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
      return self.username


