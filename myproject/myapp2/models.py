from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length = 8)
    name = models.CharField(max_length = 25)
    age = models.IntegerField()
