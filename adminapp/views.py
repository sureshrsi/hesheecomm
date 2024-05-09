from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def signup(request):
    return HttpResponse("signup testing")


def login(request):
    return HttpResponse("login testing")
