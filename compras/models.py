from django.db import models
from recetas.models import Materia_prima
from django.db.models import Sum, F
from django.contrib import admin


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=60)
    rut = models.CharField(max_length=10)
    condicion_de_pago = models.IntegerField(null=True)
    email_oc = models.EmailField(max_length=45, default='test@example.com')
    giro = models.CharField(max_length=90, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    region = models.CharField(max_length=45, null=True, blank=True)
    ciudad = models.CharField(max_length=45, null=True, blank=True)
    comuna = models.CharField(max_length=45, null=True, blank=True)
    direccion = models.CharField(max_length=90, null=True, blank=True)
    nombre_contacto_1 = models.CharField(max_length=45, null=True, blank=True)
    email_contacto_1 = models.EmailField(max_length=45, null=True, blank=True)
    telefono_contacto_1 = models.CharField(max_length=15, null=True, blank=True)
    cargo_contacto_1 = models.CharField(max_length=45, null=True, blank=True)
    nombre_contacto_2 = models.CharField(max_length=45, null=True, blank=True)
    email_contacto_2 = models.EmailField(max_length=45, null=True, blank=True)
    telefono_contacto_2 = models.CharField(max_length=15, null=True, blank=True)
    cargo_contacto_2 = models.CharField(max_length=45, null=True, blank=True)
    info_adicional = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
       return self.razon_social

    class Meta:
        verbose_name_plural = "Proveedores"


class Orden_de_compra(models.Model):
    nro_oc = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    materias_primas = models.ManyToManyField(Materia_prima, through="Mp_Oc")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True, blank=True)

    ESTADO_RECEPCION_CHOICES = [
        ('Sin recepción', 'Sin recepción'),
        ('Recepción Parcial', 'Recepción Parcial'),
        ('Recepcionada', 'Recepcionada'),
    ]

    ESTADO_OC_CHOICES = [
        ('Abierta', 'Abierta'),
        ('Cerrada', 'Cerrada'),
    ]

    estado_recepcion = models.CharField(
        choices=ESTADO_RECEPCION_CHOICES,
        default='Sin recepción',
        max_length=20
    )
    estado_oc =models.CharField(
        choices=ESTADO_OC_CHOICES,
        default='Abierta',
        max_length=20
    )

    @property
    def precio_neto_oc(self):
        return self.items.annotate(
                    precio_neto_linea=F('cantidad') * F('precio_unitario_neto')
                ).aggregate(precio_neto_oc=Sum('precio_neto_linea'))['precio_neto_oc']

    def __str__(self):
        return str(self.nro_oc)

    class Meta:
        verbose_name_plural = "Ordenes de Compra"


class Mp_Oc(models.Model):
    nro_oc = models.ForeignKey(Orden_de_compra, related_name='items', on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(Materia_prima, on_delete=models.SET_NULL, null=True)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)
    precio_unitario_neto = models.DecimalField(decimal_places=2, max_digits=12)

    @property
    def precio_neto_linea(self):
        return self.cantidad * self.precio_unitario_neto

# ### INICIO InlineModelAdmin: Para solicitar cantidad al crear OC en Admin page.
class Mp_OcInline(admin.TabularInline):
    model = Mp_Oc
    extra = 5
    max_num = 50 #define el máximo de materias_primas que puede tener una OC.

class Orden_de_compraAdmin(admin.ModelAdmin):
    inlines = (Mp_OcInline,)
### FIN InlineModelAdmin


class Recepcion(models.Model):
    nro_recepcion = models.AutoField(primary_key=True)
    nro_oc = models.ForeignKey(Orden_de_compra, on_delete=models.SET_NULL, null=True)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    materia_prima = models.ForeignKey(Materia_prima, on_delete=models.SET_NULL, null=True)
    cantidad_recepcion = models.DecimalField(decimal_places=2, max_digits=10, null=True)

    ESTADO_RECEPCION_CHOICES = [
        ('Sin recepción', 'Sin recepción'),
        ('Recepción Parcial', 'Recepción Parcial'),
        ('Recepcionada', 'Recepcionada'),
    ]

    estado_recepcion = models.CharField(
        choices=ESTADO_RECEPCION_CHOICES,
        default='Sin recepción',
        max_length=20
    )

    class Meta:
        verbose_name_plural = "Recepciones"

    def __str__(self):
        return str(self.nro_recepcion)



