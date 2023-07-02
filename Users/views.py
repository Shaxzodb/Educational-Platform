from typing import Any, Dict
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUserModel, Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm
from Posts.models import PostModel
# Create your views here
# class ProfileView(UpdateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'account/profile.html'
    
#     # def test_func(self):
#     #     return self.get_object().user == self.request.user
            
#     # def handle_no_permission(self):
#     #     return render(self.request,'403.html')
    
#     def get_queryset(self):
#         return super().get_queryset().select_related('user')
    
#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         return super().get_context_data(**kwargs)
    

class ProfileView(DetailView):
    model = Profile
    #form_class = ProfileForm
    template_name = 'account/profile.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(slug = self.kwargs['slug'])
        user = Profile.objects.filter(slug = self.kwargs['slug'])
        
        posts = PostModel.objects.filter(user = user[0].user.id)
        context['form'] = ProfileForm(instance = profile)
        context['posts'] = posts
        return context
    def get_queryset(self):
        return super().get_queryset().select_related('user')
    
@login_required()  
def user_data_save(request, slug):
    profile = Profile.objects.get(id = request.user.id)
    form = ProfileForm(request.POST, request.FILES, instance = profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect('profile', request.user.profile.slug)
    
