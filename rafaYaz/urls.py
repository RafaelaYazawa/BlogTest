from django.urls import path, include
from . import views

# When dealing with urls, create this file first and then go to the urls.py

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('feed', views.timeline, name='feed'),
    path('post/<slug:slug>', views.post, name='post_detail'),
    path('profile/<slug:slug>', views.profile, name='profile')
]