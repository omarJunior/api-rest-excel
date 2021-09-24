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

#Clase 'HeladosSerializer'
from helados.serializers import HeladosSerializer

#Clase helado
from clase_helado import Helado

#Modelo 'Helados'
from helados.models import Helados

# Create your views here.
#Creo un ViewSet
class HeladosViewSet(viewsets.ModelViewSet):    
    queryset = Helados.objects.all().order_by('id')
    serializer_class = HeladosSerializer

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer_helados")
    def leerExcel(self, request, pK= None):
        try:
            file = request.FILES['csvHelados']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            helado = Helado(file_url)
            data = helado.addHelados()
            if data == False:
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para los helados'})
            Helados.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                heladosList = list(reader)
            json_data = []
            for index, row in enumerate(heladosList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['nombre'] = row[0]
                idDict['precio'] = row[1]
                idDict['stock'] = row[2]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data': 'Ha ocurrido un error'})