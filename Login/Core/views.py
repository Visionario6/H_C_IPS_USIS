from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Historiaclinica
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, View, TemplateView
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
# Create your views here.
def Home(request):
    data ={
        'title':'INICIO'
    }
    return render(request, 'home.html',data)


@login_required
def Products(request):

    data = {
        'form': historiaclinicaForm(),
        'title' : 'Historia Clínica'
    }
    if request.method == 'POST':
        historia_clinica_form = historiaclinicaForm(data=request.POST)
        if historia_clinica_form.is_valid():
            historia_clinica_form.save()
            messages.success(request, "Historia Clínica Guardada con Éxito")
            return redirect('verHc')
        else:
            print("Error al guardar")
    return render(request, 'products.html', data)

def VerHC (request):
    hc = Historiaclinica.objects.all()
    data = {
        'hc': hc,
        'title' : 'Historia Clínica'
    }
    return render(request, 'VerHC.html', data)

def PacienteHC (request, pk):
    Phc = get_object_or_404(Historiaclinica, paciente_id=pk)
    data = {
        'phc': Phc,
        'title' : 'Mi Historia Clínica'
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
        'form': historiaclinicaFormEdit(),
        'title' : 'Editar Historia Clínica'
    }
    editarhc = Historiaclinica.objects.get(paciente_id=pk)
    if request.method == 'POST':
        form = historiaclinicaFormEdit(data=request.POST, instance=editarhc)
        if form.is_valid():
            form.save()
            messages.success(request, "Historia Clínica Editada con Éxito")
            return redirect('verHc')
        else:
            messages.error(request, "Error al editar Historia Clínica")

    return render(request, 'editarhc.html', data)

def Exit(request):
    logout(request)
    return redirect('Home')

def register(request):
    data = {
        'form': CustomUserCreationForm(),
        'title' : 'REGISTRARSE'
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Usuario Creado con Éxito")
            return redirect('Home')

        else:
            messages.error(request, "Error al crear Usuario")
            return redirect('Home')

    return render(request, 'register.html', data)

def editar_usuario(request, pk):
    data = {
        'form': EditUser(),
        'title': 'Editar Usuario'
    }
    usuario = User.objects.get(id=pk)
    if request.method == 'POST':
        user_creation_formedit = EditUser(request.POST, request.FILES, instance=usuario)
        if user_creation_formedit.is_valid():
            user_creation_formedit.save()
            messages.success(request, "Usuario Editado con Éxito")
            return redirect('Home')
        else:
            messages.error(request, "Error al editar el usuario")
    return render(request, 'editar_usuario.html', data)

def Cambiar_contraseña(request,pk):
    data={
        'form':ChangePassForm(),
        'title' : 'Editar Usuario'
    }
    usuario = User.objects.get(id=pk)
    if request.method == 'POST':
        user_creation_form = ChangePassForm(data=request.POST, instance=usuario)

        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.success(request, "Contraseña Editada Con Éxito")
            return redirect('Home')
        else:
            messages.error(request, "Error al Editar Contraseña")
    return render(request, 'cambiarcontraseña.html', data)
def Citas(request):
    data={
        'title' : 'CITAS'
    }
    return render(request, 'citas.html', data)

class PacientePdf(View):
    def get(self,request,*args,**kwargs):
        template = get_template('Pacientepdf.html')
        context ={
            'phc':  Historiaclinica.objects.get(pk=self.kwargs['pk']),
        }
        template.render()
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="HistoriaClínica.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        return response


def handler404(request, exception):
    return render(request, 'error_404.html')

def Reporte (request):
    us = User.objects.all()
    data = {
        'us': us,
        'title' : 'Reporte Usuarios'
    }
    return render(request, 'reporteusuarios.html', data)


def ReporteHC (request):
    hcp = Historiaclinica.objects.all()
    data = {
        'hcp': hcp,
        'title' : 'Reporte Historias'
    }
    return render(request, 'reportehc.html', data)


def editarRol (request, pk):

    data = {
        'form': EditRol(),
        'title' : 'Editar Rol Usuarios'
    }
    editarrol = User.objects.get(id=pk)
    if request.method == 'POST':
        formeditrol = EditRol(data=request.POST, instance=editarrol)
        if formeditrol.is_valid():
            formeditrol.save()
            messages.success(request, "Rol editado con éxito")
            return redirect('reporte')
        else:
            messages.error(request, "Error al editar Rol")

    return render(request, 'editarrol.html', data)
