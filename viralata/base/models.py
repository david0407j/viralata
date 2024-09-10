# models.py
from django.db import models
from django.utils.text import slugify


class Projeto(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Foto(models.Model):
    projeto = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name="fotos", null=True, blank=True
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fotos/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
