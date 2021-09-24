from rest_framework import serializers
from calificaciones.models import Calificaciones

class CalificacionesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Calificaciones
		fields = ['id', 'codinst', 'nombreinstitucion', 'codigomunicipio', 'nombremunicipio', 'departamento', 'calendario', 'naturaleza', 'jornada', 'evaluados','periodo']
		extra_kwargs = {'id': {'required': False}}