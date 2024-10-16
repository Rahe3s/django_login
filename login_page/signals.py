from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile1

@receiver(post_save,sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        profile1.objects.create(user=instance)
        print('profile created')

@receiver(post_save,sender=User)
def create_profile(instance, created, **kwargs):
    if created == False:
        instance.profile1.save()
        print('profile updated')
