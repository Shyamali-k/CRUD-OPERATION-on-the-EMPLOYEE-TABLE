from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    
    mobileno=models.IntegerField()
    jobprofile=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    

