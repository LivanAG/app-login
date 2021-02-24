from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
app_name='Controlador'
urlpatterns = [
    path('', IndexView.as_view(),name="index"),
    path('Login/', IniciarSesion.as_view(),name="login"),
    path('Registro/', RegistrarView.as_view(),name="registro"),
    path('CerrarSesion/',LogoutView.as_view(), name="logout"),
    path('Home/', HomeView.as_view(),name="home"),

]
