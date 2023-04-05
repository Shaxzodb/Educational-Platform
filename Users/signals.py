from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUserModel, Profile


@receiver(post_save, sender = Profile) # ! save this
def profile_save_user(sender, instance, **kwargs):
    user = instance.user
    profile = Profile.objects.get(user = user)
    user.last_name = profile.last_name or 'None'
    user.first_name = profile.first_name or 'None'
    user.email = profile.email
    user.phone = profile.phone
    user.save()

@receiver(post_delete, sender = Profile) # ! delete this
def profile_delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

@receiver(post_save, sender = CustomUserModel) # ! add and save this
def user_create_profile(sender, instance, created, **kwargs):
    try:
        Profile.objects.filter(
            user = instance
        ).update(
            last_name = instance.last_name,
            first_name = instance.first_name,
            email = instance.email,
            phone = instance.phone,
        )
    except:
        pass
    
    if created:
        Profile.objects.create(
            user = instance,
            email = instance.email
        )