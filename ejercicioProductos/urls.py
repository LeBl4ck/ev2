"""
URL configuration for ejercicioProductos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('electronica/', electronica),
    path('jugueteria/', juguetes),
    path('ropa/', ropa),
    path('meme2/', meme2),
    path('meme1/', meme1),
    path('meme3/', meme3),
]