from rest_framework import serializers

from .models import Clase, Socio, Disciplina


class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ["id", "numero", "nombre", "correo", "vence_membresia"]


class ClaseSerializer(serializers.ModelSerializer):
    disciplina = serializers.SlugRelatedField(
        slug_field="nombre",
        queryset=Disciplina.objects.all(),
    )
    inscritos = serializers.SlugRelatedField(many=True, read_only=True, slug_field="numero")

    class Meta:
        model = Clase
        fields = [
            "id",
            "codigo",
            "disciplina",
            "instructor",
            "dia",
            "hora",
            "cupo",
            "estado",
            "sala",
            "inscritos",
        ]
