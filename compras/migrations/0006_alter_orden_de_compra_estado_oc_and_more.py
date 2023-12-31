# Generated by Django 4.2.1 on 2023-06-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_estado_oc_estado_recepcion_orden_de_compra_estado_oc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_de_compra',
            name='estado_oc',
            field=models.CharField(choices=[('Abierta', 'Abierta'), ('Cerrada', 'Cerrada')], default='Abierta', max_length=20),
        ),
        migrations.AlterField(
            model_name='orden_de_compra',
            name='estado_recepcion',
            field=models.CharField(choices=[('Sin recepción', 'Sin recepción'), ('Recepción Parcial', 'Recepción Parcial'), ('Recepcionada', 'Recepcionada')], default='Sin recepción', max_length=20),
        ),
        migrations.DeleteModel(
            name='Estado_OC',
        ),
        migrations.DeleteModel(
            name='Estado_Recepcion',
        ),
    ]
