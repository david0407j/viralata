from django.shortcuts import render, get_object_or_404
from .models import Foto, Projeto


def galeria(request):
    titulo = "Galeria"
    template_name = "base/galeria.html"
    fotos = Foto.objects.filter(projeto__slug="galeria")
    projetos = Projeto.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "projetos": projetos, "titulo": titulo},
    )


def galeria_arte(request, slug):
    titulo = "Arte"
    template_name = "base/arte.html"
    fotos = Foto.objects.filter(projeto__slug=slug)
    projetos = Projeto.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "projetos": projetos, "titulo": titulo},
    )


def galeria_projeto(request, slug):
    projeto = get_object_or_404(Projeto, slug=slug)
    titulo = f"Projeto: {projeto.nome}"
    template_name = "base/projeto.html"
    fotos = Foto.objects.filter(projeto=projeto)
    projetos = Projeto.objects.all()

    return render(
        request,
        template_name,
        {"fotos": fotos, "projetos": projetos, "titulo": titulo, "projeto": projeto},
    )
