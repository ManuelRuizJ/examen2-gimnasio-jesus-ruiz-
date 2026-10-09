from django.urls import path

from . import views

urlpatterns = [
    path("", views.clase_lista, name="clase_lista"),
    path("clases/<int:pk>/", views.clase_detalle, name="clase_detalle"),
    path("clases/buscar/", views.clase_buscar, name="clase_buscar"),
]
