# Generated by Django 4.1.7 on 2023-07-06 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0019_seccion_fecha_vencimiento_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avance',
            name='contenido',
            field=models.IntegerField(),
        ),
    ]
