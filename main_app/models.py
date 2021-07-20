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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authors_detail', kwargs={"pk": self.id})

class Sighting(models.Model):
    class Meta:
        ordering = ["-date"]
        
    SIGHTINGS = (
        ("R", "Early Morning"),
        ("M", "Midday"),
        ("E", "Evening")
    )
    date = models.DateField()
    sighting = models.CharField(max_length=1, choices = SIGHTINGS, default = SIGHTINGS[0][0])

    scp = models.ForeignKey(SCP, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_sighting_display()} on {self.date}"