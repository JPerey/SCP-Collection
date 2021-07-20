from django.shortcuts import render
from .models import SCP

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def scp_index(request):
    scps = SCP.objects.all()
    return render(request,"scp/index.html", {"scps": scps})

def scp_detail(request, scp_id):
    scp = SCP.objects.get(id=scp_id)
    return render(request, "scp/detail.html", {"scp": scp})