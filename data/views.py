from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

import sqlite3

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for data"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'data/index.html', context)

def reporting(request):
    """The home page for reporting"""
    return render(request, 'data/reporting.html')

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
