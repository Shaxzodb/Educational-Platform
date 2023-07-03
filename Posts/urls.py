from django.urls import path,include
from .views import create_post
urlpatterns = [
    path('/post', create_post, name='create_post'),
]
