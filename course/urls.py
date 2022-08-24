from django.urls import path
from . import views
from course.views import  HomePageView

app_name = "course"

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.HomePageView, name='HomePageView'),
    
]



