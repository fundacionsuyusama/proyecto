# Generated by Django 4.1.7 on 2023-06-19 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0010_actividad_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=400)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.actividad')),
            ],
        ),
    ]
