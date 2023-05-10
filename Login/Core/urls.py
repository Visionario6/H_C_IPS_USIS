from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='Home'),
    path('RegistrarHistoriaClinica/', Products, name='Productos'),
    path('logout/', Exit, name='Exit'),
    path('Registro/', register, name='Register'),
    path('editarusuario/<int:pk>/', editar_usuario, name='Editar_Usuarios'),
    path('cambiarcontraseña/<int:pk>',Cambiar_contraseña, name='Cambiar_Contraseña'),
    path('citas/', Citas, name='Citas'),
    path('VerHistoriaClinica/', VerHC, name='verHc'),
    path('editarHistoriaClinica/<int:pk>/', editarHc, name='Editar_HC'),
    path('VerHistoriaClinicaPaciente/<int:pk>/', PacienteHC, name='Paciente_HC'),
    path('VerHistoriaClinicaPaciente/<int:pk>/', MineHC, name='Minehc'),
    path('pacientepdf/<int:pk>/', PacientePdf.as_view(), name='Pacientepdf'),
    path('reporte/', Reporte, name='reporte'),
    path('reportehc/', ReporteHC, name='reportehc'),
    path('editarRolUsuario/<int:pk>/', editarRol, name='Editar_rol'),
]