from django.db import models

# Create your models here.
class acc(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    username = models.CharField(max_length = 20)
    dob = models.DateField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username