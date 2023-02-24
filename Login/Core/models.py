from django.db import models
from Users.models import User
# Create your models here.
class Historia_Clinica(models.Model):
    Paciente = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Antecedentes = models.TextField(max_length=150, blank=True, null=True, unique=True)
    Epicrisis = models.TextField(max_length=150, blank=True, null=True, unique=True)
    Diagnostico = models.TextField(max_length=150, blank=True, null=True, unique=True)
    Tratamientos = models.TextField(max_length=150, blank=True, null=True, unique=True)
    Recomendaciones = models.TextField(max_length=150, blank=True, null=True, unique=True)
