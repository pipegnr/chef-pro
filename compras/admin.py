from django.contrib import admin
from. models import Proveedor, Orden_de_compra, Orden_de_compraAdmin, Mp_Oc, Recepcion


class Mp_OcInline(admin.TabularInline):
    model = Mp_Oc
    extra = 0 # set the number of extra forms to display to 0

class Orden_de_compraAdmin(admin.ModelAdmin):
    inlines = [Mp_OcInline]
    list_display = ('nro_oc', 'proveedor', 'fecha_creacion', 'precio_neto_oc', 'estado_oc', 'estado_recepcion')

    def precio_neto_oc(self, obj):
        return obj.precio_neto_oc
    precio_neto_oc.short_description = 'Precio Neto'  # Sets column name in admin interface

class RecepcionAdmin(admin.ModelAdmin):
    list_display = ('nro_recepcion', 'nro_oc', 'fecha_recepcion', 'materia_prima', 'cantidad_recepcion')

admin.site.register(Proveedor)
admin.site.register(Orden_de_compra, Orden_de_compraAdmin)
admin.site.register(Recepcion, RecepcionAdmin)
