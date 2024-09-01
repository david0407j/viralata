from django.shortcuts import render
from .models import Foto, Categoria


def galeria(request):
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        fotos = Foto.objects.filter(categoria_id=categoria_id)
    else:
        fotos = Foto.objects.all()

    categorias = Categoria.objects.all()
    return render(
        request, "base/galeria.html", {"fotos": fotos, "categorias": categorias}
    )
