from django.urls import path
from .views import ProfileView,user_data_save
urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name = 'profile'),
    path('profile/user-data-save/<slug:slug>/', user_data_save, name = 'save'),
   
]