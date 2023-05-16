# Generated by Django 4.1.7 on 2023-04-25 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0003_remove_historiaclinica_cedula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='id',
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
