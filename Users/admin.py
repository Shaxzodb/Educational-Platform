from django.contrib import admin
from .models import CustomUserModel, Profile


# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class CustomUserAdmin(admin.ModelAdmin):
    pass
