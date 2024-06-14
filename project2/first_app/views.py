from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, "first_app/home.html")