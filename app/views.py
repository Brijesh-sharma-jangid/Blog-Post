from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html', {'title':"msg"})
