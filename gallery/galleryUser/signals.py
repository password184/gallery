from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import About



def createProfile(sender, instance, created, **kwargs):
  print('Profile signal triggered')
  if created:
    user = instance
    about = About.objects.create(
      user=user,
      username=user.username,
      email=user.email,
      name=user.first_name,
    )
def updateUser(sender, instance, created, **kwargs):
  about = instance
  user = about.user

  if created == False:
    user.first_name = about.name
    user.username = about.username
    user.email = about.email
    user.save()

   

    
def deleteUser(sender, instance, **kwargs):
  user = instance.user
  user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=About)
post_delete.connect(deleteUser, sender=About)