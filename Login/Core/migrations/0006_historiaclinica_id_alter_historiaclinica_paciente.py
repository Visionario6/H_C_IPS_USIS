# Generated by Django 4.1.7 on 2023-03-15 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0005_historiaclinica_delete_historia_clinica'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='id',
            field=models.BigAutoField(auto_created=True, default='exit', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
