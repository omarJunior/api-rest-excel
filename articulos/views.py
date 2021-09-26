from django.shortcuts import render
import os

from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action #decorador

import csv

#Articulos serializer
from articulos.serializers import ArticuloSerializers

from articulos.models import Articulos

from clase_articulo import Articulo

#defaulstorage
from django.core.files.storage import default_storage

# Create your views here.
class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all().order_by('id')
    serializer_class = ArticuloSerializers

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer_articulos")
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvArticulos']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/","")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            articulos = Articulo(file_url)
            data = articulos.addArticulos()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los articulos'})
            Articulos.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                articulosList = list(reader)

            json_data = []
            for index, row in enumerate(articulosList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['nombre'] = row[0]
                idDict['precio'] = row[1]
                idDict['iva'] = row[2]
                idDict['descripcion'] = row[3]
                idDict['stock'] = row[4]
                idDict['cantidad'] = row[5]
                idDict['tipo'] = row[6]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)

        except:
            return Response({'Data':'Ha ocurrido un error xD'})