# Generated by Django 4.1.7 on 2023-05-04 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0004_remove_historiaclinica_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='antecedentes',
            field=models.CharField(blank=True, help_text='Este campo no es de carácter obligatorio y depende de la condición de cada paciente.', max_length=10000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='diagnostico',
            field=models.CharField(blank=True, help_text='Este campo no es de carácter obligatorio y depende de la condición de cada paciente.', max_length=10000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='epicrisis',
            field=models.CharField(blank=True, help_text='Este campo no es de carácter obligatorio y depende de la condición de cada paciente.', max_length=10000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(help_text='OBLIGATORIO. Seleccione el paciente al cual va a registrarle una historia clínica nueva.', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='recomendaciones',
            field=models.CharField(blank=True, help_text='Este campo no es de carácter obligatorio y depende de la condición de cada paciente.', max_length=10000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='tratamientos',
            field=models.CharField(blank=True, help_text='Este campo no es de carácter obligatorio y depende de la condición de cada paciente.', max_length=10000, null=True, unique=True),
        ),
    ]
