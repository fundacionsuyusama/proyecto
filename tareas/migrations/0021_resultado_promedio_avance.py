# Generated by Django 4.1.7 on 2023-07-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0020_alter_avance_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='promedio_avance',
            field=models.FloatField(default=0),
        ),
    ]