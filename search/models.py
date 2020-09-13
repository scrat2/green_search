# from django.db import models
from djongo import models

# Create your models here.


class Student(models.Model):
    lastname = models.CharField(max_length=30, null=False)
    firstname = models.CharField(max_length=20, null=False)
    speciality = models.CharField(max_length=3, null=False)
    address = models.CharField(max_length=50, null=False)
    postal_code = models.CharField(max_length=5, null=False)
    city = models.CharField(max_length=20, null=False)
    photo = models.ImageField(upload_to='search/static/search/images/', null=True)
    count = models.IntegerField(default=0)
    objects = models.DjongoManager()
