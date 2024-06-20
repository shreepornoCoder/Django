from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Hello, I am in Home Page")