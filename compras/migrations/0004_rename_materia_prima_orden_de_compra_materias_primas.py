# Generated by Django 4.2.1 on 2023-06-24 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_rename_q_mp_oc_mp_oc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden_de_compra',
            old_name='materia_prima',
            new_name='materias_primas',
        ),
    ]
