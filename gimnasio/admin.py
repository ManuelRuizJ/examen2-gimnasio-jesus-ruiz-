from django.contrib import admin
from django.db.models import Count

from .models import Clase, Disciplina, Socio


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ["numero", "nombre", "correo", "vence_membresia"]
    search_fields = ["numero", "nombre"]


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ["codigo", "disciplina", "dia", "hora", "instructor", "cupo", "total_inscritos", "estado"]
    list_filter = ["disciplina", "dia", "estado"]
    search_fields = ["codigo", "instructor"]
    filter_horizontal = ["inscritos"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(n=Count("inscritos"))

    @admin.display(description="Inscritos", ordering="n")
    def total_inscritos(self, obj):
        return obj.n
