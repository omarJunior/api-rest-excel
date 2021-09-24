from rest_framework import serializers
from productos.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Productos
		fields = ['id', 'codigo', 'productoName', 'precio', 'stock', 'unidad', 'descuento', 'total']
		extra_kwargs = {'id': {'required': False}}