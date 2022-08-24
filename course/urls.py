from django.urls import path
from . import views
from course.views import  HomePageView , register_request

app_name = "course"

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.HomePageView, name='HomePageView'),
    
    # path('register/', register_request.as_view(), name='register'),
    
]



