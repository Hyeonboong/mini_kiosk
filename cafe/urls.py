# cafe/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.rich_cafe, name ='menu'),
    
]