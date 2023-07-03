from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        fields = ['post']
        model = PostModel