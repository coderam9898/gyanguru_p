from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    
    template_name = "main_pages/landing.html"


def index(request):
    return HttpResponse("Hello, world.")