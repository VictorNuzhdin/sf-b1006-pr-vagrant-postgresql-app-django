#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render


# Create your views here.

## v2:
##      from django.shortcuts import render
#
def index(request):
  context = { 'version': 'v20230513.1' }
  return render(request, 'bonus/holidays.html', context)


## v1
## dependencies:
##      from django.http import HttpResponse
##      from django.template import loader
#
def index__v1(request):
  template = loader.get_template('bonus/holidays.html')
  return HttpResponse(template.render())
