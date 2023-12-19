from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    date=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=15)
    pincode=models.CharField(max_length=15)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    