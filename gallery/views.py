from django.shortcuts import render

def index(request):
    """The gallery page for thatsmoreofit"""
    return render(request, 'gallery/index.html')

def albums(request):
    return render(request, 'gallery/albums.html')
