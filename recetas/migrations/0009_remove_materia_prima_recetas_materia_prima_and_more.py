# Generated by Django 4.2.1 on 2023-06-21 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0008_materia_prima_recetas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia_prima_recetas',
            name='materia_prima',
        ),
        migrations.RemoveField(
            model_name='materia_prima_recetas',
            name='receta',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='ingredientes',
        ),
        migrations.AlterModelOptions(
            name='unidad_de_medida',
            options={'verbose_name_plural': 'Materia Prima'},
        ),
        migrations.DeleteModel(
            name='Materia_prima',
        ),
        migrations.DeleteModel(
            name='Materia_prima_Recetas',
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
    ]
