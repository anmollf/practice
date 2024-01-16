from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This is app 3")

def hello(request):
    return HttpResponse("Hello from app 3")