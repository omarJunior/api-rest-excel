from django.shortcuts import render
import os
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import csv

#Clase 'CalificacionesSerializer'
from calificaciones.serializers import CalificacionesSerializer


#Clase cliente
from clase_calificacion import Calificacion

#Modelo 'calificaciones'
from calificaciones.models import Calificaciones

from django.core.files.storage import default_storage

# Create your views here.
#Creo un ViewSet
class CalificacionesViewSet(viewsets.ModelViewSet):    
    queryset = Calificaciones.objects.all().order_by('id')
    serializer_class = CalificacionesSerializer

    @action(detail=False, methods=['post'], url_path="leer-csv", url_name="leer_calificaciones")
    def leerExcel(self, request, pK=None):
        try:
            file = request.FILES['csvCalificaciones']
            file_name = default_storage.save(file.name, file)
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            file_url = file_url.replace("/", "")
            file_url = f"C:\\Programacion\\django\\apiRest\\{file_url}"
            calificacion = Calificacion(file_url)
            data = calificacion.addCalificacion()
            if data == False:
                file.close()
                os.remove(file_url)
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para las calificaciones'})
            Calificaciones.objects.bulk_create(data)
            with open(file_url, 'rU') as csv_data:
                reader = csv.reader(csv_data, delimiter=";", quotechar='"')
                calificacionesList = list(reader)
            json_data = []
            for index, row in enumerate(calificacionesList):
                if index == 0:
                    continue
                idDict = dict()
                idDict['codinst'] = row[0]
                idDict['nombreinstitucion'] = row[1]
                idDict['codigomunicipio'] = row[2]
                idDict['nombremunicipio'] = row[3]
                idDict['departamento'] = row[4]
                idDict['calendario'] = row[5]
                idDict['naturaleza'] = row[6]
                idDict['jornada'] = row[7]
                idDict['promediomatematica'] = row[8]
                idDict['promedioquimica'] = row[9]
                idDict['promediofisica'] = row[10]
                idDict['promediobiologia'] = row[11]
                idDict['promediofilosofia'] = row[12]
                idDict['promedioingles'] = row[13]
                idDict['promediolenguaje'] = row[14]
                idDict['promediosociales'] = row[15]
                idDict['desviacionmatematica'] = row[16]
                idDict['desviacionquimica'] = row[17]
                idDict['desviacionfisica'] = row[18]
                idDict['desviacionbiologia'] = row[19]
                idDict['desviacionfilosofia'] = row[20]
                idDict['desviacioningles'] = row[21]
                idDict['desviacionlenguaje'] = row[22]
                idDict['desviacionsociales'] = row[23]
                idDict['evaluados'] = row[24]
                idDict['periodo'] = row[25]
                json_data.append(idDict)
            file.close()
            os.remove(file_url)
            return Response(json_data)
        except:
            return Response({'Data': 'Ha ocurrido un error xD'})
