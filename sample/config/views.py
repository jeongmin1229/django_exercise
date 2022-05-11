from django.http import HttpResponse, JsonResponse

# request는 필수
def user(request):
    return HttpResponse('<h1>안녕<h1>')

def info(request):
    data = {'age':30, 'name':'kim'}
    return JsonResponse(data)