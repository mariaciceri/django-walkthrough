from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse(request.method)
    else:
        return HttpResponse("You must have POSTed something")
