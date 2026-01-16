from django.contrib import admin
from .models import Profile, Post

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['username']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'is_published']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)