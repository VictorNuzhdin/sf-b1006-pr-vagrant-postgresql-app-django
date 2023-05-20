"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('hello/', include('greetings.urls')),
    path('bonus/', include('bonus.urls')),
    path('admin/', admin.site.urls),
]

# example1
#   URL1:
#       http://192.168.0.71:8000
#   OUT1: 
#       Index page
#
#   URL2:
#       http://192.168.0.71:8000/hello
#   OUT2: 
#       Hello page
#
