from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    salary = models.IntegerField()
    age = models.IntegerField()