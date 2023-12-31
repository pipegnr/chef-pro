# Generated by Django 4.2.1 on 2023-06-24 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orden_de_compra',
            options={'verbose_name_plural': 'Ordenes de Compra'},
        ),
        migrations.AlterField(
            model_name='q_mp_oc',
            name='nro_oc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='compras.orden_de_compra'),
        ),
        migrations.AlterField(
            model_name='q_mp_oc',
            name='precio_unitario_neto',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
