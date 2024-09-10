from django.contrib import admin
from .models import Foto, Projeto

admin.site.register(
    Foto,
)
admin.site.register(Projeto)


class FotoAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "projeto")  # Mostra 'name', 'slug' e 'projeto'
    list_filter = ("projeto",)  # Filtra por projeto (campo de ForeignKey)
    search_fields = (
        "name",
        "description",
        "projeto__nome",
    )  # Busca por 'name', 'description' e 'projeto__nome'

    def projeto(self, obj):
        return obj.projeto.nome

    projeto.admin_order_field = "projeto__nome"  # Ordena pelo nome da projeto
    projeto.short_description = "Projeto"  # Nome mostrado no admin
