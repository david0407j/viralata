from django.contrib import admin
from .models import Foto


@admin.register(Foto)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
