from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Home, name='Home'),
    path('RegistrarHistoriaClinica/', Products, name='Productos'),
    path('logout/', Exit, name='Exit'),
    path('Registro/', register, name='Register'),
    path('editarusuario/<int:pk>/', editar_usuario, name='Editar_Usuarios'),
    path('citas/', Citas, name='Citas'),
    path('VerHistoriaClinica/', VerHC, name='verHc'),
    path('editarHistoriaClinica/<int:pk>/', editarHc, name='Editar_HC'),
    path('VerHistoriaClinicaPaciente/<int:pk>/', PacienteHC, name='Paciente_HC'),
    path('VerHistoriaClinicaPaciente/<int:pk>/', MineHC, name='Minehc'),
    path('reiniciar/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
    path('reiniciar/enviar', auth_views.PasswordResetDoneView.as_view(), name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='pass_reset_confirm'),
    path('reiniciar/completo', auth_views.PasswordResetCompleteView.as_view(), name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('pacientepdf/<int:pk>/', PacientePdf.as_view(), name='Pacientepdf'),

]