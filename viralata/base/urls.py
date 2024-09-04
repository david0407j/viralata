from django.urls import path
from . import views


app_name = "base"


urlpatterns = [
    path("galeria/", views.galeria, name="galeria"),
    path("arte/", views.galeria_arte, name="arte"),
    path("projeto/", views.galeria_projeto, name="projeto"),
]
