from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse


# Create your models here.
class acc(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    username = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 40)
    dob = models.DateField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='images/')
    # usr = models.OneToOneField(User, on_delete= models.CASCADE, null = True, blank = True)

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("account/", kwargs={"pk": self.pk})