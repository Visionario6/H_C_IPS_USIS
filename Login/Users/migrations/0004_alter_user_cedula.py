# Generated by Django 4.1.7 on 2023-02-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_user_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(help_text='Requerido. Únicamente números. Sin puntos ni comas', max_length=11),
        ),
    ]
