# Generated by Django 4.2.1 on 2023-06-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_de_compra',
            name='nro_oc',
            field=models.AutoField(default=1000, primary_key=True, serialize=False),
        ),
    ]
