"""thatsmoreofit URL Configuration"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
    path('data/', include('data.urls')),
    path('', include('home.urls')),

]
