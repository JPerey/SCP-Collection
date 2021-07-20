from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("scp/", views.scp_index, name="index"),
    path("scps/<int:scp_id>/add_sighting", views.add_sighting, name="add_sighting"),
    path("scp/<int:scp_id>/", views.scp_detail, name="detail"),
    path("scps/create/", views.SCPCreate.as_view(), name="scps_create"),
    path("scps/<int:pk>/update", views.SCPUpdate.as_view(), name="scps_update"),
    path("scps/<int:pk>/delete", views.SCPDelete.as_view(), name="scps_delete"),
    path("author/", views.author_index, name="author_index"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("authors/create/", views.AuthorCreate.as_view(), name="authors_create"),
    path("authors/<int:pk>/update", views.AuthorUpdate.as_view(), name="authors_update"),
    path("authors/<int:pk>/delete", views.AuthorDelete.as_view(), name="authors_delete"),

]