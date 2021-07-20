from django.contrib import admin

# Register your models here.

from .models import SCP, Author, Sighting

admin.site.register(SCP)
admin.site.register(Author)
admin.site.register(Sighting)