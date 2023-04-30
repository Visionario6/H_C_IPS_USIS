from django import forms
from django.contrib.auth.forms import UserCreationForm
from Users.models import User
from .models import Historiaclinica

class  CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','cedula', 'password1', 'password2']

class historiaclinicaForm(forms.ModelForm):
    class Meta:
        model = Historiaclinica
        fields = '__all__'

class historiaclinicaFormEdit(forms.ModelForm):
    class Meta:
        model = Historiaclinica
        fields = ['antecedentes', 'epicrisis', 'diagnostico', 'tratamientos', 'recomendaciones']

