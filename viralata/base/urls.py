from django.urls import path
from . import views

urlpatterns = [
    path("galeria/", views.galeria, name="galeria"),
    path("arte/", views.galeria, name="arte"),
    path("projeto/", views.galeria, name="projeto"),
]
