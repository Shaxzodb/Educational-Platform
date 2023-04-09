from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUserModel, Profile
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm

# Create your views here
class ProfileView(UserPassesTestMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile.html'
    def get_queryset(self):
        return super().get_queryset().select_related('user')
    def test_func(self):
        return self.get_object().user.id == self.request.user.id