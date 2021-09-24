from django.shortcuts import render
import os
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import csv

#Clase 'ClientesSerializer'
from clientes.serializers import ClientesSerializer

#Modelo 'clientes'
from clientes.models import Clientes

#Clase Cliente
from clase_cliente import Cliente

from django.core.files.storage import default_storage

# Create your views here.
#Creo un ViewSet
class ClientesViewSet(viewsets.ModelViewSet):    
    queryset = Clientes.objects.all().order_by('id')
    serializer_class = ClientesSerializer
    
    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer_clientes")
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvClientes']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            clientes = Cliente(file_url)
            data = clientes.addClientes()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los clientes'})
            Clientes.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                clientesList = list(reader)
            json_data = []
            for index,row in enumerate(clientesList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['nombre'] = row[0]
                idDict['apellido'] = row[1]
                idDict['direccion'] = row[2]
                idDict['telefono'] = row[3]
                idDict['correo'] = row[4]
                idDict['ciudad'] = row[5]
                idDict['empresa'] = row[6]
                idDict['estatus'] = row[7]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data' : 'Ha ocurrido un error xD'})

