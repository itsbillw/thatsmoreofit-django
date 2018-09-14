from django.shortcuts import render

def index(request):
    """The data homepage for thatsmoreofit"""
    return render(request, 'data/index.html')

def new(request):
    return render(request, 'data/new.html')
