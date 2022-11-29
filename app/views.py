from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def welcome_template(request):
    return render(request, 'hello.html', {'msg': 'Hello World!!!'})

def welcome(request):
    return JsonResponse({'Message': 'Hello World!!!'})