# Generated by Django 4.2.1 on 2023-06-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_remove_proveedor_condicion_de_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='condicion_de_pago',
            field=models.IntegerField(null=True),
        ),
    ]
