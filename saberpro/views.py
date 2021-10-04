from django.shortcuts import render
import csv
import os

#rest_framework
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

#Modelo
from saberpro.models import SaberPro

from clase_saberPro import Saber_pro

#Serializer
from saberpro.serializers import SaberProSerializers

from django.core.files.storage import default_storage


# Create your views here.
class SaberProViewSet(viewsets.ModelViewSet):
    queryset = SaberPro.objects.all().order_by('id')
    serializer_class = SaberProSerializers

    @action(detail=False, methods=['post'], url_path='leer-csv', url_name='leer_saberPro')
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvSaberPro']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            saber_pro = Saber_pro(file_url)
            data = saber_pro.addSaberPro()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para las pruebas!'})
            csv_data = data[0]
            longitud_data = data[1]
            SaberPro.objects.bulk_create(csv_data)
            last_item = SaberPro.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)
        except:
            return Response({'Data' : 'Ha ocurrido un error!'})

        



