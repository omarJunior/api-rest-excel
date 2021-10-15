from django.db.models import fields
from rest_framework import serializers
from concesionario.models import Concesionario

class ConcesionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concesionario
        fields = ['id', 'codigo', 'nombre', 'direccion', 'ciudad', 'tipo', 'cantidad_vehiculos', 'descripcion', 'renta', 'cordinador']
        extra_kwargs = {'id': {'required': False}}