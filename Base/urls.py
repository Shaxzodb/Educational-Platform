from django.urls import path
from .views import BaseView, SettingsView

urlpatterns = [
    #path('', BaseView.as_view(), name = 'base'),
    path('settings/', SettingsView.as_view(), name = 'settings'),
]
