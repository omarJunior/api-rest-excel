from django.contrib import admin
from calificaciones.models import Calificaciones

# Register your models here.
class CalificacionesAdmin(admin.ModelAdmin):
    list_display=('codinst','nombreinstitucion','nombremunicipio','departamento','calendario')
    list_filter=('nombreinstitucion',)
    search_fields=('departamento',)

admin.site.register(Calificaciones, CalificacionesAdmin)



