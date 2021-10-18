from django.shortcuts import render
import os
# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

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
                return Response({'Data' : 'Formato incorrecto, porfavor insertar un formato correcto para las calificaciones!'})
            csv_data = data[0] 
            longitud_data = data[1]
            Calificaciones.objects.bulk_create(csv_data)
            last_item = Calificaciones.objects.all().order_by('-id')[:longitud_data].values()
            file.close()
            os.remove(file_url)
            return Response(last_item)
        except:
            return Response({'Data': 'Ha ocurrido un error!'})
