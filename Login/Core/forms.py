from django import forms
from django.contrib.auth.forms import UserCreationForm
from Users.models import User
from .models import Historia_Clinica

class  CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'cedula', 'password1', 'password2']

class Historia_Clinica_Form(forms.ModelForm):
    class Meta:
        model = Historia_Clinica
        fields = '__all__'
