from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length = 4, primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    dob = models.DateField()
    salary = models.IntegerField()
    address = models.CharField(max_length = 50)
    role = models.CharField(max_length = 15)
    doj = models.DateField()

    def __str__(self):
        return self.emp_id