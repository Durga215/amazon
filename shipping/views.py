from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import data2
def index1(request):
    mymembers = data2.objects.all()
    template = loader.get_template('index1.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))
