from django.contrib import admin

from . import models

admin.site.site_title = "Mascota"
admin.site.site_header = "Panchitos Veterinaria"


@admin.register(models.MascotaCategoria)
class MascotaCategoriaAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)

@admin.register(models.Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "raza",
        "descripcion",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre",
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"