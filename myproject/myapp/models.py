from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length = 8)
    name = models.CharField(max_length = 30)
    issue = models.DateField()