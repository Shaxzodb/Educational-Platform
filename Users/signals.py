from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUserModel, Profile
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    try:
        provider_data = SocialAccount.objects.get(user=user)
        if provider_data.provider == 'google':
            user.last_name = provider_data.extra_data['family_name']
            user.first_name = provider_data.extra_data['given_name']
            user.save()
            profile = Profile.objects.get(user = user)
            profile.location = provider_data.extra_data['locale']
            profile.user_pic = provider_data.extra_data['picture']
            profile.save()
        if provider_data.provider == 'facebook':
            user.last_name = provider_data.extra_data['last_name']
            user.first_name = provider_data.extra_data['first_name']
            user.save()
        if provider_data.provider == 'github':
            user.last_name = provider_data.extra_data['name']
            user.save()
            profile = Profile.objects.get(user = user)
            profile.location = provider_data.extra_data['location']
            profile.user_pic = provider_data.extra_data['avatar_url']
            profile.bio = provider_data.extra_data['bio']
            profile.website = provider_data.extra_data['blog']
            profile.save()
    except:
        pass

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