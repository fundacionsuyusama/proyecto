# Generated by Django 4.1.7 on 2023-10-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0036_actividad_urgente_seccion_resultado_proceso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='nombre',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='nombre',
            field=models.TextField(),
        ),
    ]
