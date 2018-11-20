from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.urls import reverse

import sqlite3

from .models import Topic, Entry, Document
from .forms import TopicForm, EntryForm, DocumentForm

def index(request):
    return render(request, 'data/index.html')

def datalog(request):
    """The home page for data"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'data/datalog.html', context)

def reporting(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('data:reporting'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'data/reporting.html', {'documents': documents, 'form': form})

def converter(request):
    return render(request, 'data/convert.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'data/topics.html', context)

def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'data/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.save()
            return HttpResponseRedirect(reverse('data:topics'))

    context = {'form': form}
    return render(request, 'data/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new event for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('data:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'data/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing event."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current event.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'data/edit_entry.html', context)
