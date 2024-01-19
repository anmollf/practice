from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import acc

# Create your views here.
def Login(request):
    return render(request,'account/login.html')

def Signup(request):    
    return render(request,'account/signup.html')

def Account(request):
    if request.method == "POST":
        print(request.FILES)
        f = request.POST.get("firstName")
        l = request.POST.get("lastName")
        u = request.POST.get("username")
        e = request.POST.get("email")
        d = request.POST.get("dob")
        p = request.FILES.get("profilePhoto")
        person = acc(fname = f, lname = l, username = u, email = e, dob = d, photo = p)
        person.save()
        context = {"Account": person, 'media_url': settings.MEDIA_URL, }
    return render(request,'account/display.html',context)