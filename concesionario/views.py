from django.shortcuts import render
import os
import csv

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

#Clase serializer
from concesionario.serializers import ConcesionarioSerializer

#Clase concesionario
from clase_concesionario import Concesionario_clase

#Modelo de concesionario
from concesionario.models import Concesionario

from django.core.files.storage import default_storage


# Create your views here.
class ConcesionarioViewSet(viewsets.ModelViewSet):
    queryset = Concesionario.objects.all().order_by('id')
    serializer_class  = ConcesionarioSerializer

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer_concesionario")
    def leerExcel(self, request, pk=None):
        try:
            file = request.FILES['csvConcesionario']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            concesionario = Concesionario_clase(file_url)
            data = concesionario.addConcesionario()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para el concesionario!'})
            csv_data = data[0] 
            longitud_data = data[1]
            Concesionario.objects.bulk_create(csv_data)
            last_item = Concesionario.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)
        except:
            return Response({'Data': 'Ha ocurrido un error'})
