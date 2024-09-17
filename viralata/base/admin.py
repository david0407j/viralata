from django.contrib import admin
from .models import Foto, Projeto


class FotoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "projeto",
        "image",
    )  # Mostra 'name' e 'projeto'
    list_filter = ("projeto",)  # Filtro para projetos no admin
    search_fields = (
        "name",
        "description",
        "projeto__nome",
    )  # Permite busca por 'name', 'description' e 'projeto__nome'

    def projeto(self, obj):
        return obj.projeto.nome if obj.projeto else "Sem Projeto"

    projeto.admin_order_field = "projeto__nome"  # Ordena pelo nome do projeto
    projeto.short_description = "Projeto"  # Nome mostrado no admin


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug")  # Mostra 'name' e 'projeto'


# Registrando o modelo Foto com a classe personalizada FotoAdmin
admin.site.register(Foto, FotoAdmin)

# Registrando o modelo Projeto sem customização
admin.site.register(Projeto, ProjetoAdmin)
