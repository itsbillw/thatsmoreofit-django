from django.urls import path

from . import views

app_name = 'data'
urlpatterns = [
    # data page.
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]
