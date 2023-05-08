from django.db import models
from Users.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Historiaclinica(models.Model):
    paciente = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True ,help_text=(
            "OBLIGATORIO. Seleccione el paciente al cual va a registrarle una historia clínica nueva."
        ))
    antecedentes = models.CharField(max_length=10000, blank=True, null=True, unique=True,
                                    help_text=(
            "Este campo no es de carácter obligatorio y depende de la condición de cada paciente."
        ))
    epicrisis = models.CharField(max_length=10000, blank=True, null=True, unique=True,
                                    help_text=(
            "Este campo no es de carácter obligatorio y depende de la condición de cada paciente."
        ))
    diagnostico = models.CharField(max_length=10000, blank=True, null=True, unique=True,
                                    help_text=(
            "Este campo no es de carácter obligatorio y depende de la condición de cada paciente."
        ))
    tratamientos = models.CharField(max_length=10000, blank=True, null=True, unique=True,
                                    help_text=(
            "Este campo no es de carácter obligatorio y depende de la condición de cada paciente."
        ))
    recomendaciones = models.CharField(max_length=10000, blank=True, null=True, unique=True,
                                    help_text=(
            "Este campo no es de carácter obligatorio y depende de la condición de cada paciente."
        ))

    Fecha_Registro = models.DateTimeField(_('Fecha de Registro'), default=timezone.now)