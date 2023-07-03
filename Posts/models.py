from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class ABSTRACTModel(models.Model):
    created = models.DateTimeField(
        auto_now_add = True
    )
    updated = models.DateTimeField(
        auto_now = True
    )
    class Meta:
        abstract = True
        
class PostModel(ABSTRACTModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # post_pic = models.ImageField(
    #     help_text='Post Image',
    #     upload_to = 'post_pics/',
    #     blank = True, 
    #     null  = True
    # )
    post = CKEditor5Field(
        max_length = 500,
        config_name='default',
    )
    def __str__(self):
        return self.post
    
    
    