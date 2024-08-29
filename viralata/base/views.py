from django.shortcuts import render
from viralata.base.models import Foto


def galeria(request):
    fotos = Foto.objects.all()
    return render(request, "galeria.html", {"fotos": fotos})
