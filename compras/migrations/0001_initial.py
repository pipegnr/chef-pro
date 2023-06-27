# Generated by Django 4.2.1 on 2023-06-24 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recetas', '0015_alter_gramajes_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_de_compra',
            fields=[
                ('nro_oc', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=10)),
                ('giro', models.CharField(max_length=90)),
                ('pais', models.CharField(max_length=45)),
                ('region', models.CharField(max_length=45)),
                ('ciudad', models.CharField(max_length=45)),
                ('comuna', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=90)),
                ('condicion_de_pago', models.IntegerField(null=True)),
                ('nombre_contacto_1', models.CharField(max_length=45)),
                ('email_contacto_1', models.EmailField(max_length=45)),
                ('telefono_contacto_1', models.CharField(blank=True, max_length=15, null=True)),
                ('cargo_contacto_1', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre_contacto_2', models.CharField(blank=True, max_length=45, null=True)),
                ('email_contacto_2', models.EmailField(blank=True, max_length=45, null=True)),
                ('telefono_contacto_2', models.CharField(blank=True, max_length=15, null=True)),
                ('cargo_contacto_2', models.CharField(blank=True, max_length=45, null=True)),
                ('info_adicional', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Q_Mp_Oc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_unitario_neto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('materia_prima', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recetas.materia_prima')),
                ('nro_oc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.orden_de_compra')),
            ],
        ),
        migrations.AddField(
            model_name='orden_de_compra',
            name='materia_prima',
            field=models.ManyToManyField(through='compras.Q_Mp_Oc', to='recetas.materia_prima'),
        ),
        migrations.AddField(
            model_name='orden_de_compra',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='compras.proveedor'),
        ),
    ]
