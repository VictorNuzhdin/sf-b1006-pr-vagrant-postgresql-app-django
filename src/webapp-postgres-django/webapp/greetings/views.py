## marshmallow - A lightweight library for converting complex datatypes to and from native Python datatypes
#  https://pypi.org/project/marshmallow/
#  https://marshmallow.readthedocs.io/en/stable/
#  pip install marshmallow
#
import json
from marshmallow import Schema, fields
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Words


# Marshmallow Schema for user Class
class ObjectSchema(Schema):
    lang = fields.Str()
    word = fields.Str()


## View - Page with single record
## http://192.168.0.71:8000/hello/eng/
#
## v1
def result(request, lang):
    ## Check parameter value
    #print(type(lang), lang)                                ## <class 'str'> BLR  |  <class 'str'> FRA
    #
    ## Get Single Object by PrimaryKey
    #word_obj = get_object_or_404(Words, lang='FRA')        ## <class 'greetings.models.Words'> Words object (2)
    #word_obj = get_object_or_404(Words, word='hello')      ## <class 'greetings.models.Words'> Words object (1)
    #word_obj = get_object_or_404(Words, word='привет')     ## <class 'greetings.models.Words'> Words object (8)
    #word_obj = get_object_or_404(Words, lang=lang)         ## <class 'greetings.models.Words'> Words object (8)  |  если "lang" == "RUS"
    #                                                       ## <class 'greetings.models.Words'> Words object (4)  |  если "lang" == "ITA"
    word = get_object_or_404(Words, lang=lang).word         ## <class 'str'> ciao
    #
    ##=DEBUG
    #print(type(word_obj), word_obj)
    #print(type(word), word)
    #
    ##=Return rendered HTML code
    return render(request, 'greetings/resultSingleRecord.html', {'hello_word': word})
    #return render(request, 'greetings/resultSingleRecord.html', {'hello_word': 'ITA'})
    #
    ##<<DONE :: CURRENT


## v0
def result__v0(request, lang):
    template = loader.get_template('greetings/resultSingleRecord.html')
    response = "lang: %s"
    #return HttpResponse(response % lang.upper())
    return HttpResponse(template.render())
    #
    ##<<DONE
#
# example
#   URL:
#       http://192.168.0.71:8000/hello/eng/
#   OUT: 
#       lang: ENG
#


## View - Page with multiple records
## v1
def index(request):
    #word_objects = Words.objects.all()                 ## <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    word_objects = Words.objects.all().values()         ## <QuerySet [{'id': 1, 'lang': 'ENG', 'word': 'hello'}, {'id': 2, 'lang': 'FRA', 'word': 'bonjour'}, {'id': 3, 'lang': 'ESP', 'word': 'hola'}, {'id': 4, 'lang': 'ITA', 'word': 'ciao'}, {'id': 5, 'lang': 'DEU', 'word': 'hallo'}, {'id': 6, 'lang': 'UKR', 'word': 'вітаю'}, {'id': 7, 'lang': 'BLR', 'word': 'прывітанне'}, {'id': 8, 'lang': 'RUS', 'word': 'привет'}]>
    #
    context = { "data_words":  word_objects, "page_title": "All records"}
    return render(request, 'greetings/resultMultyRecords.html', context)



## v0
def index__v0_tests(request):

    #response00 = Words.objects
    #response01 = Words.objects.all()
    #response02 = Words.objects.all()[0]
    #response03 = Words.objects.all()[0].lang
    #response04 = Words.objects.all()[0].word
    #
    #sorted_asc = Words.objects.order_by('id')
    #sorted_desc = Words.objects.order_by('-id')
    #
    word_objects = Words.objects.all()
    #response11 = [w.word for w in word_objects]
    #response12 = [w.lang for w in word_objects]
    #
    #
    #print(type(response00), response00)                    ## <class 'django.db.models.manager.Manager'> greetings.Words.objects
    #print(type(response01), response01)                    ## <class 'django.db.models.query.QuerySet'> <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    
    #print(type(response02), response02)                    ## <class 'greetings.models.Words'> Words object (1)
    #print(type(response03), response03)                    ## <class 'str'> ENG
    #print(type(response04), response04)                    ## <class 'str'> hello
    #print(type(response11), response11)                    ## <class 'list'> ['hello', 'bonjour', 'hola', 'ciao', 'hallo', 'вітаю', 'прывітанне', 'привет']
    #print(type(response12), response12)                    ## <class 'list'> ['ENG', 'FRA', 'ESP', 'ITA', 'DEU', 'UKR', 'BLR', 'RUS']
    #
    #print(sorted_asc)                                      ## <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    #print(sorted_desc)                                     ## <QuerySet [<Words: Words object (8)>, <Words: Words object (7)>, <Words: Words object (6)>, <Words: Words object (5)>, <Words: Words object (4)>, <Words: Words object (3)>, <Words: Words object (2)>, <Words: Words object (1)>]>

    ## Basic - Simple Response
    #response = 'Hello page'
    #response = '<h1>Test</h1>'

    ## Advanced - JSON Response
    # Marshmallow - objects list to JSON
    object_schema = ObjectSchema()
    json_string = object_schema.dumps(word_objects, many=True, ensure_ascii=False)   ## <class 'str'> [{"lang": "ENG", "word": "hello"}, {"lang": "FRA", "word": "bonjour"}, {"lang": "ESP", "word": "hola"}, {"lang": "ITA", "word": "ciao"}, {"lang": "DEU", "word": "hallo"}, {"lang": "UKR", "word": "вітаю"}, {"lang": "BLR", "word": "прывітанне"}, {"lang": "RUS", "word": "привет"}]
    #response = json_string
    

    ## Advanced - Python Dictionary Response
    #response = json.loads(json_string)
    #print(type(response), response)                       ## <class 'list'> [{'lang': 'ENG', 'word': 'hello'}, {'lang': 'FRA', 'word': 'bonjour'}, {'lang': 'ESP', 'word': 'hola'}, {'lang': 'ITA', 'word': 'ciao'}, {'lang': 'DEU', 'word': 'hallo'}, {'lang': 'UKR', 'word': 'вітаю'}, {'lang': 'BLR', 'word': 'прывітанне'}, {'lang': 'RUS', 'word': 'привет'}]

    ## Test: List Response
    #response = [1, 2, 3, 4]                               ## displays: 1234

    ## Test: Mutable structures
    #response = {"1", "2", "3", "4"}                       ## displays: 1234  or   1432   or  2413

    ## Test: Strange behavior
    #response = {"a": 1, "b": 2, "c": 3}                   ## page displays only "abc"
    #print(response['a'])                                  ## 1
    #
    #response = {"a": ["ENG", "FRA", "RUS"]}               ## page displays only "a"
    #print(response['a'])                                  ## ['ENG', 'FRA', 'RUS']
    #print(response['a'][0])                               ## ENG

    ##=Подключаем шаблоны/templates
    ## https://www.w3schools.com/django/django_templates.php
	## 1. создаем файлы html-шаблонов/template
    ##    webapp/greetings/templates/resultSingleRecord.html
    ##    webapp/greetings/templates/resultMultyRecords.html
    ## 2. импортируем необходимые компоненты
    ##    from django.template import loader
    ## 3. загружаем шаблон
    ##    template = loader.get_template('myfirst.html')
    ## 4. возвращаем HTTP Ответ с обработанным шаблоном
    ##    return HttpResponse(template.render())
    #
    template = loader.get_template('greetings/resultMultyRecords.html')

    ## Return HttpResponse Object
    return HttpResponse(template.render())
    #return HttpResponse(content=response, content_type="application/json", charset="utf-8")
    #return HttpResponse(content=response, status=200, content_type='text/html; charset="utf-8"', charset="utf-8")
    #return HttpResponse(response)
