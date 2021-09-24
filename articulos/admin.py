from django.contrib import admin
from articulos.models import Articulos

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombres','precio','iva','descripcion','stock','cantidad','tipo')
    list_filter = ('nombres','stock',)
    search_fields = ('nombres',)
admin.site.register(Articulos, ArticuloAdmin)    

