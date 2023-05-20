## Templates processing
## - Django Add Test View
##   https://www.w3schools.com/django/django_test_view.php
##
import os
import datetime as dt
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
#from django.templatetags.static import static
from greetings.models import Words


# View - Home/Index page __v3
def index(request):
    #
    page_title = "Home"                                                                 ## Page text
    #
    #version_file = open(static('APP_VERSION'), "r")
    #print(version_file.readline())
    #                                                                                   ## Get App version from file
    #print(os.path.abspath(os.getcwd()))                                                ## /opt/webapp-postgres-django
    #print(os.path.abspath(os.getcwd()) + '/webapp/APP_VERSION')                        ## /opt/webapp-postgres-django/webapp/APP_VERSION
    version_file = open(os.path.abspath(os.getcwd()) + '/webapp/APP_VERSION', 'r')      ## <_io.TextIOWrapper name='/opt/webapp-postgres-django/webapp/APP_VERSION' mode='r' encoding='UTF-8'>
    app_version = version_file.readline()                                               ## 202230512.1
    version_file.close()
    #
    dt_now = dt.datetime.now()                                          ## Current time
    ts = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    #
    word_objects = Words.objects.all().values()                         ## <QuerySet [{'id': 1, 'lang': 'ENG', 'word': 'hello'}, {'id': 2, 'lang': 'FRA', 'word': 'bonjour'}, {'id': 3, 'lang': 'ESP', 'word': 'hola'}, {'id': 4, 'lang': 'ITA', 'word': 'ciao'}, {'id': 5, 'lang': 'DEU', 'word': 'hallo'}, {'id': 6, 'lang': 'UKR', 'word': 'вітаю'}, {'id': 7, 'lang': 'BLR', 'word': 'прывітанне'}, {'id': 8, 'lang': 'RUS', 'word': 'привет'}]>
    #print(type(word_objects[0]), word_objects[0])                      ## <class 'dict'> {'id': 1, 'lang': 'ENG', 'word': 'hello'}
    #print(word_objects[0]['id'])                                       ## 1
    #
    langs = [w.lang for w in Words.objects.all().order_by('lang')]      ## ['BLR', 'DEU', 'ENG', 'ESP', 'FRA', 'ITA', 'RUS', 'UKR']
    #print(type(langs), langs)                                          ## <class 'list'> ['BLR', 'DEU', 'ENG', 'ESP', 'FRA', 'ITA', 'RUS', 'UKR']
    #
    template = loader.get_template('home/home.html')
    #
    #page_data  = {'languages': 'ENG | FRA | ESP | ITA | DEU | UKR | BLR | RUS', 'ts': ts}
    page_data  = {'languages': langs, 'app_ts': ts, 'app_version': app_version}
    context= {
        'page_title': page_title,
        'page_data': page_data,
        'words_data': word_objects,
    }
    # Return HTTP response contains HTML code with injected data
    return HttpResponse(template.render(context, request))


# View - Home/Index page __v2
def index__v2(request):
    #
    page_title = "Home"                             ## Page text
    dt_now = dt.datetime.now()                      ## Current time
    ts = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    #
    page_data  = {'languages': 'ENG | FRA | ESP | ITA | DEU | UKR | BLR | RUS', 'ts': ts}
    context= {
        'page_title': page_title,
        'page_data': page_data,
    }
    # Return HTTP response contains HTML code with injected data
    template_path = 'home/home.html'
    return render(request, template_path, context)


# View - Home/Index page __v1
def index__v1(request):
    message = "Home page"
    #
    template = loader.get_template('home/home.html')
    #template = loader.get_template('index.html')
    #
    # Return HTTP response contains HTML code with injected data
    return HttpResponse(template.render())
    #return HttpResponse(template.render())
    #return HttpResponse("Home page")
#
# example1
#   URL1:
#       http://192.168.0.71:8000
#   OUT1: 
#       Home page
#
