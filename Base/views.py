from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BaseView(TemplateView):
    template_name:str = 'base.html'
