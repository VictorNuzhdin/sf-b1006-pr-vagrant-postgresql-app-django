#import json
from marshmallow import Schema, fields                              ## pip install marshmallow
#from django.shortcuts import render
from django.http import HttpResponse
from .models import Words


# Schema for marshmallow
class ObjectSchema(Schema):
    lang = fields.Str()
    word = fields.Str()



# Create your views here.
def index(request):
 
    #response_test = Words.objects                                  ## greetings.Words.objects
    #response_test = Words.objects[0]                               ## ERROR :: TypeError: 'Manager' object does not support indexing
    #response_test = Words.objects.all()                            ## <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    #response_test = type(Words.objects.all())                      ## <class 'django.db.models.query.QuerySet'>
    #response_test = Words.objects.all()[0]                         ## Words object (1)
    #
    #response_test = Words.objects.order_by('id')                   ## <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    #response_test = Words.objects.order_by('-id')                  ## объекты выводятся в обратном направлении - от последнего к первому по id
    #response_test = Words.objects.order_by('id')[0]                ## Words object (1)
    #response_test = Words.objects.order_by('id')[1]                ## Words object (2)
    #response_test = Words.objects.order_by('id')[1].lang           ## FRA
    #response_test = Words.objects.order_by('id')[1].word           ## bonjour
    #
    word_objects = Words.objects.all()
    #response_test = [w.word for w in word_objects]                 ## <class 'list'> ['hello', 'bonjour', 'hola', 'ciao', 'hallo', 'вітаю', 'прывітанне', 'привет']
    #response_test = [w.lang for w in word_objects]                 ## <class 'list'> ['ENG', 'FRA', 'ESP', 'ITA', 'DEU', 'UKR', 'BLR', 'RUS']
    #response_test = ', '.join([w.word for w in word_objects])      ## <class 'str'> hello, bonjour, hola, ciao, hallo, вітаю, прывітанне, привет
    #response_test = ', '.join([w.lang for w in word_objects])      ## <class 'str'> ENG, FRA, ESP, ITA, DEU, UKR, BLR, RUS
    #
    #import json
    #jsonStr = json.dumps([obj.__dict__ for obj in word_objects])   ## ERROR :: TypeError: Object of type 'ModelState' is not JSON serializable
    #response_test = jsonStr
    #
    #from marshmallow import Schema, fields
    object_schema = ObjectSchema()
    #json_string = object_schema.dumps(word_objects, many=True)     ## <class 'str'> [{}, {}, {}, {}, {}, {}, {}, {}]
    #                                                               ## <class 'str'> [{"lang": "ENG", "word": "hello"}, {"lang": "FRA", "word": "bonjour"}, {"lang": "ESP", "word": "hola"}, {"lang": "ITA", "word": "ciao"}, {"lang": "DEU", "word": "hallo"}, {"lang": "UKR", "word": "\u0432\u0456\u0442\u0430\u044e"}, {"lang": "BLR", "word": "\u043f\u0440\u044b\u0432\u0456\u0442\u0430\u043d\u043d\u0435"}, {"lang": "RUS", "word": "\u043f\u0440\u0438\u0432\u0435\u0442"}]
    #
    json_string = object_schema.dumps(word_objects, many=True, ensure_ascii=False)   ## <class 'str'> [{"lang": "ENG", "word": "hello"}, {"lang": "FRA", "word": "bonjour"}, {"lang": "ESP", "word": "hola"}, {"lang": "ITA", "word": "ciao"}, {"lang": "DEU", "word": "hallo"}, {"lang": "UKR", "word": "вітаю"}, {"lang": "BLR", "word": "прывітанне"}, {"lang": "RUS", "word": "привет"}]
    response_test = json_string
    response_json = json_string

    #
    #print(type(response_test), response_test)
    print(response_test)

    response = '<h1>Test</h1>'
    #return HttpResponse(response, status=200, content_type="text/html", charset="utf-8")
    #
    # JSON Formatter & Validator
    #https://jsonformatter.curiousconcept.com/#
    return HttpResponse(response_json, content_type="application/json", charset="utf-8")
    #
    #

    #=ПОЛНАЯ_ХУЙНЯ (искажает исходное форматирование)
    # JsonResponse objects
    # https://docs.djangoproject.com/en/4.2/ref/request-response/
    #from django.http import JsonResponse
    #return JsonResponse(json_string, safe=False, json_dumps_params={'ensure_ascii':False})                 ## "[{\"word\": \"hello\", \"lang\": \"ENG\"}, {\"word\": \"bonjour\", \"lang\": \"FRA\"}, {\"word\": \"hola\", \"lang\": \"ESP\"}, {\"word\": \"ciao\", \"lang\": \"ITA\"}, {\"word\": \"hallo\", \"lang\": \"DEU\"}, {\"word\": \"вітаю\", \"lang\": \"UKR\"}, {\"word\": \"прывітанне\", \"lang\": \"BLR\"}, {\"word\": \"привет\", \"lang\": \"RUS\"}]"
                                                                                                            ## хуйня какаято

    ##=ОШИБКИ_ИСПРАВЛЕНИЯ
    #return HttpResponse(response, 200, content_type='text/html; charset=utf-8')                            ## ERROR: TypeError: __init__() got multiple values for argument 'content_type'
    #                              status=200, content_type='text/html', charset='utf-8'                    ## Fix
    
    #return HttpResponse('<h1>Hello</h1>', status=200, headers='content_type=text/html; charset=utf-8')     ## ERROR: dictionary update sequence element #0 has length 1; 2 is required.
    #                                                  headers={ "Header1": "value1", "Header2": "value2"}  ## Fix
    #
    # ERROR: Кривая кодировка в браузере {"word": "Ð¿Ñ€Ð¸Ð²ÐµÑ‚", "lang": "RUS"}, браузер не распознал автоматический кодировку кириллицы
    #return HttpResponse(content=response, status=200, content_type="text/html", charset="utf-8")
    # Fix:
    #return HttpResponse(content=response, status=200, content_type='text/html; charset="utf-8"', charset="utf-8")

    
    ##=РАБОТАЕТ
    #return HttpResponse("ERROR 503 : Service Unavailable", status=503, reason="The server is not ready to handle the request. Server is down for maintenance or that is overloaded")
    #return HttpResponse("ERROR 502 : Bad Gateway", status=502, reason="While Server working as a gateway to get a response needed to handle the request, got an invalid response")
    #return HttpResponse("ERROR 500 : Internal Server Error", status=500, reason="The server has encountered a situation it does not know how to handle")
    #return HttpResponse("ERROR 404 : Not Found", status=404, reason="The server cannot find the requested resource")
    #return HttpResponse("ERROR 403 : Forbidden", status=403, reason="The client does not have access rights to the content")
    #return HttpResponse("ERROR 401 : Unauthorized", status=401, reason="The client must authenticate itself to get the requested response")
    #return HttpResponse("ERROR 400 : Bad Request", status=400, reason="Malformed request syntax, invalid request message framing, or deceptive request routing")
    #
    #return HttpResponse('<h1>Hello</h1>', status=200, headers={"content_type": "text/html", "charset": "utf-8"})
    #return HttpResponse(content=b'AnyData', content_type="text/html", status=200, reason="DataSubmitted", charset="utf-8", headers={"Custom-Header1": "value1", "Custom-Header2": "value2"})
    #return HttpResponse(content=None, content_type=None, status=200, reason="EmptyResponse", charset=None, headers=None)
    #return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")
    #return HttpResponse("Hello page")


def result(request, lang):
    response = "lang: %s"
    return HttpResponse(response % lang.upper())

# example2
#   URL:
#       http://192.168.0.71:8000/hello/eng/
#   OUT: 
#       lang: ENG
#
