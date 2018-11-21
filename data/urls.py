from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'data'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Reporting page.
    path('reporting/', views.reporting, name='reporting'),

    # Reporting page.
    path('upload/', views.upload, name='upload'),

    # Reporting page.
    path('converter/', views.converter, name='converter'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic.
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new event.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an event.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
