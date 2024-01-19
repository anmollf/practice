from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This is the homepage")


def hello(request):
    context = {
        "Name": "Anmol"
    }
    return HttpResponse("Hello!")