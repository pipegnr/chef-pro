from django.db import models

# class Proveedor(models.Model):
#     razon_social = models.CharField(max_length=60)
#     rut = models.CharField(max_length=10)
#     giro = models.CharField(max_length=90)
#     pais = models.CharField(max_length=45)
##     region = models.CharField(max_length=45)
#     ciudad = models.CharField(max_length=45)
#     comuna = models.CharField(max_length=45)
#     direccion = models.CharField(max_length=90)
#     condicion_de_pago = models.IntegerField(null=True)
#     nombre_contacto_1 = models.CharField(max_length=45)
#     email_contacto_1 = models.CharField(max_length=45)
#     telefono_contacto_1 = models.CharField(max_length=15, null=True, blank=True)
#     cargo_contacto_1 = models.CharField(max_length=45, null=True, blank=True)
#     nombre_contacto_2 = models.CharField(max_length=45, null=True, blank=True)
#     email_contacto_2 = models.CharField(max_length=45, null=True, blank=True)
#     telefono_contacto_2 = models.CharField(max_length=15, null=True, blank=True)
#     cargo_contacto_2 = models.CharField(max_length=45, null=True, blank=True)
#     info_adicional = models.TextField(max_length=1000, null=True, blank=True)

#     def __str__(self):
#        return self.razon_social

#     class Meta:
#         verbose_name_plural = "Proveedores"