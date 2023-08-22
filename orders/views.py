from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import data1
def index(request):
    mymembers = data1.objects.all()
    template = loader.get_template('index.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))
