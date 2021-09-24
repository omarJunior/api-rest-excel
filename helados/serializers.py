from rest_framework import serializers
from helados.models import Helados

class HeladosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Helados
		fields = ['id', 'nombre', 'precio', 'stock']
		extra_kwargs = {'id': {'required': False}}