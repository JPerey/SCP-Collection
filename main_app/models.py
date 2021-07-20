from django.db import models
from django.urls import reverse

# Create your models here.

class SCP(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    class_type = models.CharField(max_length=10)
    description = models.TextField()
    nuetralized = models.BooleanField()
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"scp_id": self.id})

class Author(models.Model):
    name = models.CharField(max_length= 50)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"author_id": self.id})
