# Generated by Django 4.1.7 on 2023-03-15 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0006_historiaclinica_id_alter_historiaclinica_paciente'),
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
