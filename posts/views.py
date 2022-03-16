from django.shortcuts import render
from posts.models import Post

def home(request):
    posts = Post.objects.all()

    return render(request,"posts/home.html",{'posts':posts})

def about(request):
    return render(request, "posts/about.html")