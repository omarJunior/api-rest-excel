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
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los productos'})
            Productos.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                heladosList = list(reader)
            json_data = []
            for index, row in enumerate(heladosList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['codigo'] = row[0]
                idDict['NombreProducto'] = row[1]
                idDict['precio'] = row[2]
                idDict['stock'] = row[3]
                idDict['unidad'] = row[4]
                idDict['descuento'] = row[5]
                idDict['total'] = row[6]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data': 'Ha ocurrido un error'})
        
