from django.shortcuts import render

from .models import Photo

def index(request):
    """The gallery page for thatsmoreofit - Show all"""
    photos = Photo.objects.order_by('date_added')
    context = {'photos': photos}
    return render(request, 'gallery/index.html', context)
