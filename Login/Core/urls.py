from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='Home'),
    path('productos/', Products, name='Productos'),
    path('logout/', Exit, name='Exit'),
    path('Registro/', register, name='Register'),
    path('editarusuario/<int:pk>/', editar_usuario, name='Editar_Usuarios'),
    path('citas/', Citas, name='Citas'),
    path('VerHistoriaClinica/',VerHC, name='verHc')
]