from django.shortcuts import render, get_object_or_404
from . models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')

def timeline(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'timeline.html', context=context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'post.html', {
        'post': post
    })