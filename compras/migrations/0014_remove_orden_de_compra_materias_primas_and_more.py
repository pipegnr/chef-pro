# Generated by Django 4.2.1 on 2023-06-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_alter_orden_de_compra_nro_oc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden_de_compra',
            name='materias_primas',
        ),
        migrations.RemoveField(
            model_name='orden_de_compra',
            name='proveedor',
        ),
        migrations.DeleteModel(
            name='Mp_Oc',
        ),
        migrations.DeleteModel(
            name='Orden_de_compra',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]