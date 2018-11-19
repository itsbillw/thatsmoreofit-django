from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import DocumentForm
from .models import Document

def index(request):
    """The gallery page for thatsmoreofit - Show all"""
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'gallery/index.html', context)

@login_required
def photo_upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('gallery:index'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'gallery/upload.html', {'documents': documents, 'form': form})
