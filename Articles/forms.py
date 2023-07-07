from django import forms
from .models import ArticleModel
from django_ckeditor_5.widgets import CKEditor5Widget
class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title_at','content_at','image_at']
        widgets = {
            'title_at':forms.TextInput(attrs={'placeholder':'Article Title','style':'border:none !important;','class':'shadow-none mb-3 p-0'}),
            'image_at':forms.FileInput(attrs={'style':'','class':'shadow-none'}),
            'content_at':CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}
            )
        }
        
