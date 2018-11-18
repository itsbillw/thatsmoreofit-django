from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Photo

def index(request):
    """The gallery page for thatsmoreofit - Show all"""
    photos = Photo.objects.order_by('date_added')
    context = {'photos': photos}
    return render(request, 'gallery/index.html', context)

@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'gallery/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'gallery/simple_upload.html')
