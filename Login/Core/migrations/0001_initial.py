# Generated by Django 4.1.7 on 2023-02-23 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.TextField(blank=True, max_length=333, null=True)),
                ('n2', models.TextField(blank=True, max_length=333, null=True)),
                ('n3', models.TextField(blank=True, max_length=333, null=True)),
                ('n4', models.TextField(blank=True, max_length=333, null=True)),
                ('n5', models.TextField(blank=True, max_length=333, null=True)),
                ('Persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]