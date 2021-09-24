from django.shortcuts import render
import csv
import os
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.files.storage import default_storage

#Clase 'VehiculosSerializer'
from vehiculos.serializers import VehiculosSerializer

from clase_vehiculo import Vehiculo

#Modelo 'Vehiculos'
from vehiculos.models import Vehiculos

# Create your views here.
#Creo un ViewSet
class VehiculosViewSet(viewsets.ModelViewSet):    
    queryset = Vehiculos.objects.all().order_by('id')
    serializer_class = VehiculosSerializer

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leerVehiculos")
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvVehiculos']            
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            vehi = Vehiculo(file_url)
            vehiculo = vehi.addVehiculos()
            if vehiculo == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los vehiculos'})
            Vehiculos.objects.bulk_create(vehiculo)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                vehiculosList = list(reader)
            json_data = []
            for index, row in enumerate(vehiculosList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['placa'] = row[0]
                idDict['modelo'] = row[1]
                idDict['marca'] = row[2]
                idDict['color'] = row[3]
                idDict['precio'] = row[4]
                idDict['descripcion'] = row[5]
                json_data.append(idDict)

            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data': 'Ha ocurrido un error'})