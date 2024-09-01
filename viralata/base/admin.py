from django.contrib import admin
from .models import Foto, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "categoria", "image_thumbnail")
    search_fields = ("name", "description")
    list_filter = ("categoria", "description")
    readonly_fields = ("image_thumbnail",)
    fields = (
        "name",
        "image",
        "description",
        "categoria",
        "image_thumbnail",
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "No image"

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Imagem"
