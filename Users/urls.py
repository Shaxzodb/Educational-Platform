from django.urls import path
from .views import ProfileView
urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name = 'profile'),
]