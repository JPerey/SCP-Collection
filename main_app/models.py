from django.db import models

# Create your models here.

class SCP(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    class_type = models.CharField(max_length=10)
    description = models.TextField()
    nuetralized = models.BooleanField()
    