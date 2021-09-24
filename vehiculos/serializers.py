from rest_framework import serializers
from vehiculos.models import Vehiculos

class VehiculosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vehiculos
		fields = ['id', 'placa', 'modelo', 'marca', 'color', 'precio', 'descripcion']
		extra_kwargs = {'id': {'required': False}}