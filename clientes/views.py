from django.shortcuts import render
import os

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

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
    def leerExcel(self, request, pk=None):
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
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los clientes!'})
            csv_data = data[0] 
            longitud_data = data[1]
            Clientes.objects.bulk_create(csv_data)
            last_item = Clientes.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)
        except:
            return Response({'Data' : 'Ha ocurrido un error!'})


