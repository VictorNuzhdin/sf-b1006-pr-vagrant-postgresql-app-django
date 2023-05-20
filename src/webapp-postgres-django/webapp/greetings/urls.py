from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                 ## example: /hello/
    path('<str:lang>/', views.result, name='result'),    ## example: /hello/ENG/
]
#
# example2
#   URL:
#       http://192.168.0.71:8000/hello/ENG/
#   OUT: 
#       lang: ENG
#
