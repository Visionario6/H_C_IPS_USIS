from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from Core.models import *

# Create your models here.
class User(AbstractUser, AbstractBaseUser, PermissionsMixin):
    ROL_CHOICES = [
        ('PA', 'PACIENTE'),
        ('ES', 'ESPECIALISTA')
    ]
    cedula = models.CharField(max_length=11, verbose_name='Cédula', blank=False, help_text=(
            "Requerido. Únicamente números. Sin puntos ni comas"
        ))
    is_especialista = models.BooleanField(
        ("Especialista status"),
        default=False
    )

    def Nombreuser(self):
        return "{} {} - {}".format(self.first_name,self.last_name,self.cedula)

    def __str__(self):
        return self.Nombreuser()