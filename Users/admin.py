from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, Profile
from django.utils.html import format_html
from django.templatetags.static import static
import csv
from django.http import HttpResponse

# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

style = 'object-fit: cover; border-radius: 100%;'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin, ExportCsvMixin):
    def thumb(self, obj):
        if obj.user_pic:
            if str(obj.user_pic).startswith("https://"):
                return format_html(f"<img src='{str(obj.user_pic)}' style='{style}' width='35' height='35' />")
            else:
                return format_html(f"<img src='{str(obj.user_pic.url)}' style='{style}' width='35' height='35' />")
        return format_html(f"<img src={static('img/user_default_pic.png')} style='{style}' width='35' height='35' />")

    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'
    fieldsets = (
        (
            'General',
            {
                'fields' : (
                    'user',
                    'email',
                    'phone',
                    'last_name',
                    'first_name'
                )
            }
        ),
        (
            'Bios',
            {
                'fields' : (    
                    'bio',
                    'slug'
                )
            }
        ),
    
        (
            'Addition',
            {
                'fields' : (
                    'headshot_image',
                    'user_pic',
                    'location',
                    'website',
                    'birth_date',
                )
            }
        ),
        (
            'Friends',
            {
                'fields' : (
                    'friends',  
                )
            }
        ),
    )
    ordering = ['-user__last_login']
    actions = ["export_as_csv"]
    list_display = ['thumb','user','email','phone','last_name','first_name']
    list_per_page = 25
   
    
    def headshot_image(self, obj):
        if obj.user_pic:
            if str(obj.user_pic).startswith("https://"):
                return format_html(f"<img src='{str(obj.user_pic)}' width='300px'/>")
            else:
                return format_html(f"<img src='{str(obj.user_pic.url)}' width='300px'/>")
        return format_html("<img src='{url}' width='300px'/>".format(url = static('img/user_default_pic.png')))
    
    # Tanlangan Deleteni olib Tashlash
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    change_list_template = "admin/change_list.html"
    
    # Faqat O'qish uchun
    readonly_fields = ["slug","headshot_image"]
    #readonly_fields = ["slug","friends","headshot_image"]
    
@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin, ExportCsvMixin):
    
    def thumb(self, obj):
        if obj.profile.user_pic:
            if str(obj.profile.user_pic).startswith("https://"):
                return format_html(f"<img src='{str(obj.profile.user_pic)}' style='{style}' width='35' height='35' />")
            else:
                return format_html(f"<img src='{str(obj.profile.user_pic.url)}'style='{style}' width='35' height='35' />")
        return format_html(f"<img class='p-0 m-0 border' src={static('img/user_default_pic.png')} style='{style}' width='35' height='35' />")
    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Addition',
            {
                'fields' : (
                    'phone',
                    'email',
                    'confirm'
                )
            }
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            'Addition',
            {
                'fields' : (
                    'phone',
                    'email_verification',
                    'confirm'
                )
            }
        ),
    )

    list_display = ['thumb','username','phone','is_staff','confirm','email_verification']
    list_filter = ['is_active','is_staff','is_superuser','confirm','email_verification']
   
    search_fields = ['username','email','phone','last_name','first_name']
    ordering = ['-username']
    actions = ["export_as_csv"]
    list_per_page = 25
    
    change_list_template = "admin/change_list.html"
