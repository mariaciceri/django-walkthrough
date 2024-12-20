from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):
    return HttpResponse("Hello, world from about!")
