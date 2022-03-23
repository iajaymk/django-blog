from django.shortcuts import render, get_object_or_404
from posts.models import Post

def home(request):
    posts = Post.objects.all()

    return render(request,"posts/home.html",{'posts':posts})

def about(request):
    return render(request, "posts/about.html")


def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)

    return render(request,"posts/detail.html",{'post':post})
