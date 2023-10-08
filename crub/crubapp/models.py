from django.db import models

 
# Create your models here.
class Datas(models.Model):
    name = models.CharField(default="",max_length=20)
    age = models.IntegerField(default="")
    dob = models.DateField(default="")
    email = models.CharField(default="",max_length=50)
    phone_no = models.IntegerField(default="")