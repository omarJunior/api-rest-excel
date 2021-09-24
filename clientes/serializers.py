from rest_framework import serializers
from clientes.models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clientes
		fields = ['id', 'nombres', 'apellidos', 'direccion', 'telefono', 'correo', 'ciudad', 'empresa', 'estatus']
		extra_kwargs = {'id': {'required': False}}