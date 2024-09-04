from django.contrib import admin
from .models import Foto, Categoria

admin.site.register(
    Foto,
)
admin.site.register(Categoria)


class FotoAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "categoria")  # Mostra 'name', 'slug' e 'categoria'
    list_filter = ("categoria",)  # Filtra por categoria (campo de ForeignKey)
    search_fields = (
        "name",
        "description",
        "categoria__nome",
    )  # Busca por 'name', 'description' e 'categoria__nome'

    def categoria(self, obj):
        return obj.categoria.nome

    categoria.admin_order_field = "categoria__nome"  # Ordena pelo nome da categoria
    categoria.short_description = "Categoria"  # Nome mostrado no admin
