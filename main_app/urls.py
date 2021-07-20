from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("scp/", views.scp_index, name="index"),
    path('scp/<int:scp_id>/', views.scp_detail, name="detail"),

]