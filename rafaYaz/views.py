from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from . models import Post, Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def timeline(request):
    posts = Post.objects.order_by('-published_at')
    context = {
        "posts": posts
    }
    return render(request, 'timeline.html', context=context)

@login_required
def post(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'post.html', {
        'post': post
    })

def profile(request, slug):
    user = get_object_or_404(Profile, user__username=slug)
    return render(request, 'profile.html', {
        'profile': user
    })
