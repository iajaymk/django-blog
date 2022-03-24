from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Category
from .forms import CommentForm 


def home(request):
    posts = Post.objects.all()

    return render(request,"posts/home.html",{'posts':posts})

def about(request):
    return render(request, "posts/about.html")


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug = slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request,"posts/detail.html",{'post':post,'form':form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request,"posts/category.html",{'category': category})