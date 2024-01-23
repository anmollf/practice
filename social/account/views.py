from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AccForm
from .models import acc
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

# Create your views here.
def Login(request):
    return render(request,'account/login.html')

# def Signup(request):    
#     frm = AccForm()
#     return render(request,'account/signup.html',{"form":frm})

# def Account(request):
    # if request.method == "POST":
    #     # print(request.FILES)
    #     # f = request.POST.get("firstName")
    #     # l = request.POST.get("lastName")
    #     # u = request.POST.get("username")
    #     # e = request.POST.get("email")
    #     # d = request.POST.get("dob")
    #     # p = request.FILES.get("profilePhoto")
    #     # us = User.objects.create_user(username=u,email=e,password=request.POST.get("password"))
    #     # print(us)
    #     # person = acc(fname = f, lname = l, username = u, email = e, dob = d, photo = p)
    #     # person.save()
    #     # context = {"Account": person, 'media_url': settings.MEDIA_URL, }
    #     frm =AccForm(request.POST,request.FILES)
    #     print(request.FILES)

    #     print(frm.files)
    #     if frm.is_valid():
    #         # f = frm.cleaned_data.get("firstName")
    #         # l = frm.cleaned_data.get("lastName")
    #         # u = frm.cleaned_data.get("username")
    #         # e = frm.cleaned_data.get("email")
    #         # d = frm.cleaned_data.get("dob")
    #         # p = frm.files.get("profilePhoto")
    #         # #function to store image in directory
    #         # person = acc(fname = f, lname = l, username = u, email = e, dob = d, photo = p)
    #         person = frm.save()
    #         return render(request,'account/display.html',{"Account":person})
    #     else:
    #         print(frm.errors)
    # else:
    #     frm = AccForm()
    # return render(request,'account/signup.html',{"form":frm})

class accCreate(CreateView):
    model = acc
    # fields = "__all__"
    form_class = AccForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return f'/account/{self.object.pk}/'

class accDetails(DetailView):
    model = acc
    context_object_name = "Account"