from django.db import models
from Users.models import User
# Create your models here.
class Historiaclinica(models.Model):
    paciente = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    antecedentes = models.CharField(max_length=150, blank=True, null=True, unique=True)
    epicrisis = models.CharField(max_length=150, blank=True, null=True, unique=True)
    diagnostico = models.CharField(max_length=150, blank=True, null=True, unique=True)
    tratamientos = models.CharField(max_length=150, blank=True, null=True, unique=True)
    recomendaciones = models.CharField(max_length=150, blank=True, null=True, unique=True)