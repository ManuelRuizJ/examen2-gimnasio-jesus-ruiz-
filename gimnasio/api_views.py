from rest_framework import viewsets

from .models import Clase, Socio
from .serializers import ClaseSerializer, SocioSerializer


class SocioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer
    lookup_field = "numero"


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.select_related("disciplina").prefetch_related("inscritos")
    serializer_class = ClaseSerializer
