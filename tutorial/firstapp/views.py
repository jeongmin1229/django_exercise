from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index1(request):
    return HttpResponse('<h1>hello<h1>')

def index2(request):
    return HttpResponse('<h1>hi<h1>')