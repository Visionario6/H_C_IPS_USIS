# Generated by Django 4.1.7 on 2023-02-23 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historia_clinica',
            name='Persona',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='n1',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='n2',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='n3',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='n4',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='n5',
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Antecedentes',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Diagnostico',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Epicrisis',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Recomendaciones',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='Tratamientos',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
