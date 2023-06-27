from django.contrib import admin
from .models import Categoria_material, Subcategoria_material, Unidad_de_medida, Materia_prima, \
Categoria_receta, Receta, Gramajes, RecetaAdmin

class Materia_primaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'categoria', 'subcategoria', 'inventario', 'unidad_de_medida')

admin.site.register(Categoria_material)
admin.site.register(Subcategoria_material)
admin.site.register(Unidad_de_medida)
admin.site.register(Materia_prima, Materia_primaAdmin)
admin.site.register(Categoria_receta)
admin.site.register(Receta, RecetaAdmin)
#admin.site.register(Gramajes)
#No queremos mostrarlo, porque va dentro de RecetaAdmin
