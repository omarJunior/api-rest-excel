from django.db import models
from rest_framework import serializers
from articulos.models import Articulos

class ArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = ['nombres', 'precio', 'iva', 'descripcion', 'stock', 'cantidad', 'tipo']
        extra_kwargs = {'id': {'required': False}}