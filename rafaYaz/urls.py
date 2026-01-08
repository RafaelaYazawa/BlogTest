from django.urls import path
from . import views

# When dealing with urls, create this file first and then go to the urls.py

urlpatterns = [
    path('', views.index, name="index")
]