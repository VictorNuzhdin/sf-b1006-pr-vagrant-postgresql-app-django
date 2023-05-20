from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   ## example: /bonus
]
#
# example
#   URL:
#       http://192.168.0.71:8000/bonus
#   OUT: 
#       slideshow app
#
