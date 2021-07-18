from django.shortcuts import render

# Create your views here.

# TODO: Temp cat class for testing purposes:

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat("Lolo", "tabby", "Foul Little demon", 3),
    Cat("Sachi", "Tortoise sheel", "Diluted tortoise shell", 0),
    Cat("Raven", "Black tripod", "3 legged cat", 4),
]

# Temp SCP Class for project:

class SCP:
    def __init__(self, name, number, class_type, description, nuetralized):
        self.name = name
        self.number = number
        self.class_type = class_type
        self.description = description
        self.nuetralized = nuetralized

scps = [
    SCP("Here be dragons", "SCP-1234","Safe", "test description", True),
    SCP("Shy Guy", "SCP-5432", "Euclid", "Test Description 2", False),
]

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def scp_index(request):
    return render(request,"scp/index.html", {"scps": scps})