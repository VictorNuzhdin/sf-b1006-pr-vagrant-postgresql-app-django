## marshmallow - A lightweight library for converting complex datatypes to and from native Python datatypes
#  https://pypi.org/project/marshmallow/
#  https://marshmallow.readthedocs.io/en/stable/
#  pip install marshmallow
#
from marshmallow import Schema, fields
from django.http import HttpResponse
from .models import Words


# Marshmallow Schema for user Class
class ObjectSchema(Schema):
    lang = fields.Str()
    word = fields.Str()


# Create your views here.
def index(request):
    #
    word_objects = Words.objects.all()                                               ## <QuerySet [<Words: Words object (1)>, <Words: Words object (2)>, <Words: Words object (3)>, <Words: Words object (4)>, <Words: Words object (5)>, <Words: Words object (6)>, <Words: Words object (7)>, <Words: Words object (8)>]>
    # Marshmallow - objects list to JSON
    object_schema = ObjectSchema()
    json_string = object_schema.dumps(word_objects, many=True, ensure_ascii=False)
    #print(type(json_string), json_string)                                           ## <class 'str'> [{"lang": "ENG", "word": "hello"}, {"lang": "FRA", "word": "bonjour"}, {"lang": "ESP", "word": "hola"}, {"lang": "ITA", "word": "ciao"}, {"lang": "DEU", "word": "hallo"}, {"lang": "UKR", "word": "вітаю"}, {"lang": "BLR", "word": "прывітанне"}, {"lang": "RUS", "word": "привет"}]

    # JSON Formatter & Validator
    #https://jsonformatter.curiousconcept.com/#
    #
    return HttpResponse(content=json_string, content_type="application/json", charset="utf-8")


def result(request, lang):
    response = "lang: %s"
    return HttpResponse(response % lang.upper())

# example2
#   URL:
#       http://192.168.0.71:8000/hello/
#   OUT: 
#   [
#      {
#         "lang": "ENG",
#         "word": "hello"
#      },
#      {
#         "lang": "FRA",
#         "word": "bonjour"
#      },
#      {
#         "lang": "ESP",
#         "word": "hola"
#      },
#      {
#         "lang": "ITA",
#         "word": "ciao"
#      },
#      {
#         "lang": "DEU",
#         "word": "hallo"
#      },
#      {
#         "lang": "UKR",
#         "word": "вітаю"
#      },
#      {
#         "lang": "BLR",
#         "word": "прывітанне"
#      },
#      {
#         "lang": "RUS",
#         "word": "привет"
#      }
#   ]
#
