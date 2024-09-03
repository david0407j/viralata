from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Foto(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fotos/")
    description = models.TextField(blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="fotos"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
