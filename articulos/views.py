from django.shortcuts import render
import os

from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action #decorador

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
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los articulos!'})
            csv_data = data[0] 
            longitud_data = data[1]
            Articulos.objects.bulk_create(csv_data)
            last_item = Articulos.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)

        except:
            return Response({'Data':'Ha ocurrido un error!'})