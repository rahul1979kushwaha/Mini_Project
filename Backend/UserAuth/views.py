from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = 1
    return HttpResponse("hello")
