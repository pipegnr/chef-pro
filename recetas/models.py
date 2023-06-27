from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



class Categoria_material(models.Model):
    nombre_categoria = models.CharField(max_length=45, unique=True)
    desc_categoria = models.CharField(max_length=500, blank=True)
    class Meta:
        verbose_name_plural = "Categorias material"
    def __str__(self):
       return self.nombre_categoria
        #Por defecto, en /admin le agrega siempre una "s" al final de cada clase (lo piensa en inglés).
        #Con esta función, podemos override el nombre que aparece en /admin.

class Subcategoria_material(models.Model):
    nombre_subcategoria = models.CharField(max_length=45, unique=True)
    desc_subcategoria = models.CharField(max_length=500, blank=True)
    class Meta:
        verbose_name_plural = "Subcategorias material"
    def __str__(self):
       return self.nombre_subcategoria
        #Cuando lo llamemos, nos tirará el nombre en vez del id del objeto.

class Unidad_de_medida(models.Model):
    nombre_unidad_de_medida = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
       return self.nombre_unidad_de_medida

class Materia_prima(models.Model):
    descripcion = models.CharField(max_length=45, unique=True)
    categoria =  models.ForeignKey(Categoria_material, on_delete=models.SET_NULL, null=True)
    subcategoria =  models.ForeignKey(Subcategoria_material, on_delete=models.SET_NULL, null=True)
    unidad_de_medida = models.ForeignKey(Unidad_de_medida, on_delete=models.SET_NULL, null=True)
    merma = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Merma en %', null=True, blank=True)
    calorias = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbohidratos = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    proteina = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sodio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    azucares = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_saturada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_monosaturada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_poliinsaturada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grasa_trans = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    colesterol = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fibras = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    inventario = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True, blank=True)

    @property
    def tiene_ficha_tecnica(self):
        if self.calorias is not None and self.proteina is not None \
            and self.grasa_total is not None and self.grasa_saturada is not None \
                and self.grasa_monosaturada is not None and self.grasa_poliinsaturada is not None \
                    and self.grasa_trans is not None and self.colesterol is not None \
                        and self.carbohidratos is not None and self.azucares is not None \
                            and self.fibras is not None and self.sodio is not None:
            return "Sí"
        else:
            return "No"

    def __str__(self):
       return self.descripcion

    class Meta:
        verbose_name_plural = "Materias Primas"

class Categoria_receta(models.Model):
    nombre_categoria = models.CharField(max_length=45, unique=True)
    desc_categoria = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Categorias Receta"

    def __str__(self):
       return self.nombre_categoria

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=45, unique=True)
    categoria = models.ForeignKey(Categoria_receta, on_delete=models.SET_NULL, null=True)
    ingredientes = models.ManyToManyField(Materia_prima, through='Gramajes')
    #through es para indicar la tabla intermediaria de la relación ManyToMany (más abajo explicación).

    def __str__(self):
        return self.nombre_receta

    class Meta:
        verbose_name_plural = "Recetas"

    @property
    def all_tiene_ficha_tecnica(self):
        materias_primas = self.ingredientes.all()
        if all(mp.tiene_ficha_tecnica == "Sí" for mp in materias_primas):
            return "Sí"
        else:
            return "No"



#SECCIÓN TABLA INTERMEDIA
    #Debido a que tenemos una relación ManyToMany (Ingredientes/Recetas),
    #y que necesitamos campos extra (cantidad de cada ingrediente),
    #Debemos crear nosotros la clase intermediaria (sin que lo haga Django automáticamente)
class Gramajes(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(Materia_prima, on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        unique_together = [['receta', 'materia_prima']]
        #Con esto no se permite incluir 2 veces el mismo ingrediente en una receta.
#FIN SECCIÓN TABLA INTERMEDIA


# ### INICIO InlineModelAdmin: Para solicitar cantidad al crear receta en Admin page.
class GramajesInline(admin.TabularInline):
    model = Gramajes
    extra = 5
    max_num = 50 #define el máximo de ingredientes que puede tener un receta.

class RecetaAdmin(admin.ModelAdmin):
    inlines = (GramajesInline,)
### FIN InlineModelAdmin










