from django.shortcuts import render
from .models import Foto, Categoria


def galeria(request):
    titulo = "Galeria"
    template_name = "base/galeria.html"
    fotos = Foto.objects.all()
    categorias = Categoria.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "categorias": categorias, "titulo": titulo},
    )


def galeria_arte(request):
    titulo = "Arte"
    template_name = "base/arte.html"
    fotos = Foto.objects.filter(categoria__slug="arte")
    categorias = Categoria.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "categorias": categorias, "titulo": titulo},
    )


def galeria_projeto(request):
    titulo = "Projeto"
    template_name = "base/projeto.html"
    fotos = Foto.objects.filter(categoria__slug="projeto")
    categorias = Categoria.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "categorias": categorias, "titulo": titulo},
    )
