from django.urls import path
from . import views

urlpatterns = [
    path("",views.Hello,name = "base"),
    path("apis/",views.listAll.as_view(),name= "api"),
    path("apis/<int:id>",views.useAPI.as_view(),name= "ap"),
    path("all/",views.listAll.as_view(),name= "all"),
]