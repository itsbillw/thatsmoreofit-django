from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    # gallery page.
    path('', views.index, name='index'),
    path('upload/', views.simple_upload, name='simple_upload'),
]
