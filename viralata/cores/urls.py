from django.urls import path

from viralata.cores.views import home

app_name = "cores"
urlpatterns = [
    path("", home, name="home"),
]
