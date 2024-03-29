# Generated by Django 4.1.7 on 2023-09-27 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0033_delete_resultado2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('promedio_avance', models.FloatField(default=0)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='tareas.proyecto')),
            ],
        ),
    ]
