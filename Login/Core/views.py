from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.
def Home(request):
    return render(request, 'home.html')


@login_required
def Products(request):
    data = {
        'form': Historia_Clinica_Form()
    }
    if request.method == 'POST':
        historia_clinica_form = Historia_Clinica_Form(data=request.POST)
        if historia_clinica_form.is_valid():
            historia_clinica_form.save()
            return redirect('Home')
    return render(request, 'products.html', data)

def VerHC (request):
    return render(request,'verhc.html')
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

    return render(request, 'editar_usuario.html',data)

def Citas(request):
    return render(request, 'citas.html')