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
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para las pruebas'})
            SaberPro.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter = ";", quotechar='"')
                saber_pro_list = list(reader)
            json_data = []
            for index, row in enumerate(saber_pro_list):
                if index == 0:
                    continue
                idDict = dict()
                idDict['nombres'] = row[0]
                idDict['apellidos'] = row[1]
                idDict['genero'] = row[2]
                idDict['ciudad'] = row[3]
                idDict['matematicas'] = row[4]
                idDict['lenguaje'] = row[5]
                idDict['ciencias'] = row[6]
                idDict['ingles'] = row[7]
                idDict['ciudadanas'] = row[8]
                idDict['fisica'] = row[9]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data' : 'Ha ocurrido un error xD'})

        



