from django.urls import path
from . import views

urlpatterns = [
    path("galeria/<slug:slug>/", views.galeria, name="galeria_slug"),
    path("arte/", views.galeria, {"slug": "arte"}, name="arte"),
    path("projeto/", views.galeria, {"slug": "projeto"}, name="projeto"),
]
