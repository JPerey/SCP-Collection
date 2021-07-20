from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import SCP, Author
from .forms import SightingForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def scp_index(request):
    scps = SCP.objects.all()
    return render(request,"scp/index.html", {"scps": scps})

def add_sighting(request, scp_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.scp_id = scp_id
        new_sighting.save()
    return redirect('detail', scp_id = scp_id)

def scp_detail(request, scp_id):
    scp = SCP.objects.get(id=scp_id)
    authors_scp_doesnt_have = Author.objects.exclude(id__in = scp.authors.all().values_list("id"))
    sighting_form = SightingForm()
    return render(request, "scp/detail.html", {
        "scp": scp,
        "sighting_form": sighting_form,
        "authors": authors_scp_doesnt_have,
    })

class SCPCreate(CreateView):
    model = SCP
    fields = "__all__"

class SCPUpdate(UpdateView):
    model = SCP
    fields = ["description", "nuetralized"]

class SCPDelete(DeleteView):
    model = SCP
    success_url = "/scp/"

class AuthorList(ListView):
  model = Author

class AuthorDetail(DetailView):
  model = Author

# def author_index(request):
#     authors = Author.objects.all()
#     return render(request,"author/a_index.html", {"authors": authors})

# def author_detail(request, author_id):
#     author = Author.objects.get(id=author_id)
#     return render(request, "author/a_detail.html", {"author": author})

class AuthorCreate(CreateView):
    model = Author
    fields = "__all__"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name"]

class AuthorDelete(DeleteView):
    model = Author
    success_url = "/author/"