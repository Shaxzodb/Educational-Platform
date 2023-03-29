from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUserModel, Profile

@receiver(post_delete, sender = Profile) # delete this
def profile_delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

@receiver(post_save, sender = CustomUserModel) # add this
def user_create_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(
            user = instance,
            email = instance.email
        )