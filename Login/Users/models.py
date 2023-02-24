from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROL_CHOICES = [
        ('PA', 'PACIENTE'),
        ('ES', 'ESPECIALISTA')
    ]
    cedula = models.CharField(max_length=11, blank=False, help_text=(
            "Requerido. Únicamente números. Sin puntos ni comas"
        ))
    rol = models.CharField(max_length=2, choices=ROL_CHOICES, default='PA')