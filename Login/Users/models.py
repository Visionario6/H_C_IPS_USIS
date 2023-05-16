import os.path
import uuid

from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from Core.models import *
from PIL import Image
from Login import settings

# Create your models here.

class User(AbstractUser, AbstractBaseUser, PermissionsMixin):
    picture = models.ImageField(default='imagen_base.png', upload_to='users/', verbose_name='Foto de Perfil', null=True)
    ROL_CHOICES = [
        ('PA', 'PACIENTE'),
        ('ES', 'ESPECIALISTA')
    ]
    cedula = models.CharField(max_length=11, verbose_name='Cédula', blank=False, help_text=(
            "Obligatorio. Digite su número de cédula completo. Únicamente números. Sin puntos ni comas"
        ))
    is_especialista = models.BooleanField(
        ("Rol especialista"),
        default=False
    )

    def Nombreuser(self):
        return "{} {} - {}".format(self.first_name,self.last_name,self.cedula)

    def __str__(self):
        return self.Nombreuser()