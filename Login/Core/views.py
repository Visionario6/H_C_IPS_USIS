from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Historiaclinica
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView,View
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
# Create your views here.
def Home(request):
    return render(request, 'home.html')


@login_required
def Products(request):

    data = {
        'form': historiaclinicaForm(),
    }
    if request.method == 'POST':
        historia_clinica_form = historiaclinicaForm(data=request.POST)
        if historia_clinica_form.is_valid():
            historia_clinica_form.save()
            messages.success(request, "Historia Clinica Guardada con Éxito")
            return redirect('verHc')
        else:
            print("Error al guardar")
    return render(request, 'products.html', data)

def VerHC (request):
    hc = Historiaclinica.objects.all()
    data = {
        'hc': hc,
    }
    return render(request, 'VerHC.html', data)

def PacienteHC (request, pk):
    Phc = get_object_or_404(Historiaclinica, paciente_id=pk)
    data = {
        'phc': Phc
    }
    return render(request, 'VerHCPaciente.html', data)

def MineHC (request, pk):
    Phcm = get_object_or_404(Historiaclinica, paciente_id=pk)
    data = {
        'phcm': Phcm
    }
    return render(request, 'base.html', data)

def editarHc (request, pk):

    data = {
        'form': historiaclinicaFormEdit()
    }
    editarhc = Historiaclinica.objects.get(paciente_id=pk)
    if request.method == 'POST':
        form = historiaclinicaFormEdit(data=request.POST, instance=editarhc)
        if form.is_valid():
            form.save()
            messages.success(request, "Historia Clinica Editada con Éxito")
            return redirect('verHc')
        else:
            messages.error(request, "Error al editar Historia Clinica")

    return render(request, 'editarhc.html', data)

def Exit(request):
    logout(request)
    return redirect('Home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Usuario Creado con Éxito")

        else:
            messages.error(request, "Error al crear Usuario")
            return redirect('Home')

    return render(request, 'register.html', data)

def editar_usuario(request, pk):
    data = {
        'form': CustomUserCreationForm()
    }
    usuario = User.objects.get(id=pk)
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST, instance=usuario)

        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.success(request, "Usuario Editado con Éxito")
            return redirect('Home')
        else:
            messages.error(request, "Error al editar el usuario")
    return render(request, 'editar_usuario.html', data)

def Citas(request):
    return render(request, 'citas.html')

class PacientePdf(View):
    def get(self,request,*args,**kwargs):
        template = get_template('Pacientepdf.html')
        context ={
            'phc':  Historiaclinica.objects.get(pk=self.kwargs['pk'])
        }
        template.render()
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="HistoriaClinica.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        return response
