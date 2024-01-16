from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home2"),
    path("hello/",views.hello, name="Hello2")
]