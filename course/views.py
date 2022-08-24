from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    
    template_name = "main_pages/landing.html"
    # template_name = "main_pages/landing.html"

class CourseView(TemplateView):
    template_name= "main_pages/dashboard.html"

class signupView(TemplateView):
    template_name= "main_pages/signup.html"

def index(request):
    return HttpResponse("Hello, world.")



# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("course:dashboard")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="main_pages/register.html", context={"register_form":form})
