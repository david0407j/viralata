from django.urls import path
from . import views


app_name = "base"


urlpatterns = [
    path("galeria/", views.galeria, name="galeria"),
    path("arte/<str:slug>/", views.galeria_arte, name="arte"),
    path("projeto/<str:slug>/", views.galeria_projeto, name="projeto"),
    path("cultura/<str:slug>/", views.galeria_cultura, name="cultura"),
    path("editais/<str:slug>/", views.galeria_editais, name="editais"),
]
