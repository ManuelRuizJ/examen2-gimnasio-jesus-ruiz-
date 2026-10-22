from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import Clase, Socio
from .serializers import ClaseSerializer, SocioSerializer


class SocioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer
    lookup_field = "numero"


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.select_related("disciplina").prefetch_related("inscritos")
    serializer_class = ClaseSerializer

    @action(detail=True, methods=["post"])
    def inscribir(self, request, pk=None):
        clase = self.get_object()
        numero_socio = request.data.get("socio")

        # Verificar que se haya enviado el número del socio
        if not numero_socio:
            return Response(
                {"error": "Debes proporcionar el número del socio."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Buscar al socio
        try:
            socio = Socio.objects.get(numero=numero_socio)
        except Socio.DoesNotExist:
            return Response(
                {"error": "El socio indicado no existe."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Verificar que la clase no esté cancelada
        if clase.estado == Clase.Estado.CANCELADA:
            return Response(
                {"error": "No puedes inscribir socios en una clase cancelada."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Verificar que el socio no esté inscrito previamente
        if clase.inscritos.filter(pk=socio.pk).exists():
            return Response(
                {"error": "El socio ya está inscrito en esta clase."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Verificar que la clase tenga lugares disponibles
        if clase.inscritos.count() >= clase.cupo:
            return Response(
                {"error": "La clase ya está llena."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Verificar que la membresía siga vigente
        if socio.vence_membresia < timezone.localdate():
            return Response(
                {"error": "La membresía del socio está vencida."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inscribir al socio solamente si todas las validaciones pasan
        clase.inscritos.add(socio)

        return Response(
            self.get_serializer(clase).data,
            status=status.HTTP_200_OK,
        )