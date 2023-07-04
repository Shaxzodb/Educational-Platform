from django.urls import path
from .views import ProfileView,user_data_save, friends, friends_remove
urlpatterns = [
    path('profile/<slug:slug>/', ProfileView.as_view(), name = 'profile'),
    path('profile/user-data-save/<slug:slug>/', user_data_save, name = 'save'),
    path('friend/<slug:slug>', friends, name = 'friend'),
    path('friend-remove/<slug:slug>', friends_remove, name = 'friends_remove'),
   
]