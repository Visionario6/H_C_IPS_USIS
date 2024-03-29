# Generated by Django 4.1.7 on 2023-05-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(help_text='Obligatorio. Digite su número de cédula completo. Únicamente números. Sin puntos ni comas', max_length=11, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Obligatorio. Por Favor, digite su correo electrónico de manera completa(Respetando dominios y demás caracteres).', max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Obligatorio. Por Favor digite su nombre completo en mayúscula.', max_length=150, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Obligatorio. Por Favor digite sus apellidos completos en mayúscula.', max_length=150, verbose_name='last name'),
        ),
    ]
