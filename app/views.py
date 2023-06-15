from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    post = Post.objects.all()
    return render(request, 'app/home.html', {
        'Post' : post
    })

def about(request):
    return render(request, 'app/about.html', {'title':"msg"})
