"""apiRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Importamos Django REST Framework y la vista 
from rest_framework import routers
from calificaciones.views import CalificacionesViewSet
from clientes.views import ClientesViewSet
from helados.views import HeladosViewSet
from productos.views import ProductosViewSet
from vehiculos.views import VehiculosViewSet
from articulos.views import ArticulosViewSet
from saberpro.views import SaberProViewSet

router = routers.DefaultRouter()
router.register(r'calificaciones', CalificacionesViewSet) #Como aparecera en la ruta
router.register(r'clientes', ClientesViewSet) #Como aparecera en la ruta
#router.register(r'clientes', ClientesViewSet.as_view({'post':'leerExcel'}), basename='clientes') #Como aparecera en la ruta
router.register(r'helados', HeladosViewSet) #Como aparecera en la ruta
router.register(r'productos', ProductosViewSet) #Como aparecera en la ruta
router.register(r'vehiculos', VehiculosViewSet) #Como aparecera en la ruta
router.register(r'articulos', ArticulosViewSet)
router.register(r'saberPro', SaberProViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]