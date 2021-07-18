from django.shortcuts import render
from .models import SCP

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def scp_index(request):
    scps = SCP.objects.all()
    return render(request,"scp/index.html", {"scps": scps})