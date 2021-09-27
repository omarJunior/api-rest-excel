from django.contrib import admin
from saberpro.models import SaberPro
# Register your models here.
class SaberProAdmin(admin.ModelAdmin):
    list_display=('nombres','apellidos','genero','ciudad','matematicas', 'lenguaje','ciencias','ingles','ciudadanas','fisica')
    list_filter=('apellidos',)
    search_fields=('nombres',)

admin.site.register(SaberPro, SaberProAdmin)  
