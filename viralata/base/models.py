from django.db import models


class Foto(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fotos/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
