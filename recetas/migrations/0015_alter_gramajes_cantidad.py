# Generated by Django 4.2.1 on 2023-06-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0014_alter_categoria_material_nombre_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramajes',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
