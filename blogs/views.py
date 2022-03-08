from webbrowser import get
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogs/blog.html', {'blogs': blogs})

def home(request):
    return render(request, 'blogs/home.html')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})