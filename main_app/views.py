from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You are at the blog index")

# Create your views here.
