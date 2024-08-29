from django.urls import path

from viralata.cores.views import cores


app_name = "cores"
urlpatterns = [
    path("", cores, name="cores"),
]
