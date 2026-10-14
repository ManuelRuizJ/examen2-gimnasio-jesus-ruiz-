from rest_framework import serializers

from .models import Clase, Socio


class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ["id", "numero", "nombre", "correo", "vence_membresia"]


class ClaseSerializer(serializers.ModelSerializer):
    disciplina = serializers.StringRelatedField()
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
            "inscritos",
        ]
