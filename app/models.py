"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Nuser(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    mounth=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
class article(models.Model):
    subject=models.CharField(max_length=500)
    text=models.TextField()
    date=models.CharField(max_length=100)
    preview=models.CharField(max_length=255,blank=True)
    poster=models.TextField()