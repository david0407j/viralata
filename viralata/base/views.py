from django.shortcuts import render, get_object_or_404
from .models import Foto, Categoria


def galeria(request, slug=None):
    titulo = "Galeria"
    template_name = "base/galeria.html"

    if slug:
        categoria = get_object_or_404(Categoria, nome__iexact=slug)
        fotos = Foto.objects.filter(categoria=categoria)
        titulo = categoria.nome.capitalize()
        if slug.lower() in ["arte", "projeto"]:
            template_name = f"base/{slug}.html"
    elif "arte" in request.path:
        titulo = "Arte"
        template_name = "base/arte.html"
        fotos = Foto.objects.filter(categoria__nome__iexact="arte")
    elif "projeto" in request.path:
        titulo = "Projeto"
        template_name = "base/projeto.html"
        fotos = Foto.objects.filter(categoria__nome__iexact="projeto")
    else:
        fotos = Foto.objects.all()

    categorias = Categoria.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "categorias": categorias, "titulo": titulo},
    )
