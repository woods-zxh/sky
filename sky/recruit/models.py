

# Create your models here.
from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    introduction = models.TextField()
    selfMedia = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    depart = models.CharField(max_length=50)