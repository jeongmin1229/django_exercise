from django.http import HttpResponse
from django.shortcuts import render
from .models import Curriculum
# Create your views here.
def insert(request):
    Curriculum.objects.create(name='linux')
    c = Curriculum(name='python')
    c.save()
    Curriculum(name='python').save()
    Curriculum(name='django').save()

    return HttpResponse('데이터 입력완료')

def show(request):
    curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)
    return render(request, 'firstapp/show.html', {'data' : curriculum})


def index1(request):
    return HttpResponse('<h1>hello<h1>')

def index2(request):
    return HttpResponse('<h1>hi<h1>')