from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    # gallery page.
    path('', views.index, name='index'),
    path('albums/', views.albums, name='albums'),
]
