from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PostModel
from .forms import PostForm
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

@login_required()
def create_post(request):
    post_form = PostForm(request.POST,request.FILES)
    
    if post_form.is_valid() and request.method == 'POST':
        post_form.instance.user = request.user
        post_form.save()
    return redirect('profile', request.user.profile.slug)
    