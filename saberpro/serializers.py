from rest_framework import serializers
from saberpro.models import SaberPro

class SaberProSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaberPro
        fields = ['id','nombres','apellidos','genero','ciudad','matematicas','lenguaje','ciencias','ingles','ciudadanas','fisica']
        extra_kwargs = {'id': {'required': False}}