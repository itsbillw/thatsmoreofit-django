"""thatsmoreofit URL Configuration"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('data.urls')),
    path('gallery/', include('gallery.urls')),
    path('users/', include('users.urls')),
    path('', include('home.urls')),

]
