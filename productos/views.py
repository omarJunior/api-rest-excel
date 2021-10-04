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

#Clase 'ProductosSerializer'
from productos.serializers import ProductosSerializer

from clase_producto import Producto

#Modelo 'Productos'
from productos.models import Productos

# Create your views here.
#Creo un ViewSet
class ProductosViewSet(viewsets.ModelViewSet):    
    queryset = Productos.objects.all().order_by('id')
    serializer_class = ProductosSerializer

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer-productos")
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvProductos']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            producto = Producto(file_url)
            data = producto.addProductos()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los productos!'})
            csv_data = data[0] 
            longitud_data = data[1]
            Productos.objects.bulk_create(csv_data)
            last_item = Productos.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)
        except:
            return Response({'Data': 'Ha ocurrido un error!'})
        
