from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

# When dealing with urls, create this file first and then go to the urls.py

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('timeline', views.timeline, name='timeline'),
    path('post/<slug:slug>', views.post, name='post_detail'),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
]