from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,FormView
from .forms import *
from django.contrib.auth.forms import UserCreationForm
import os
# Create your views here.

class IndexView(TemplateView):
    template_name='Controlador/index.html'
    def get_context_data(self,*args,**kwargs):
        #l = int(os.environ.get('TIMES'))
        #k = str(os.environ.get('DATABASE_URL')
        p = os.environ.get('PRUEBA')
        context = super().get_context_data(*args,**kwargs)
        context['saludo'] = "Hola"
        context['l'] = "x"
        context['k'] = "x"
        context['p'] = p
        
        return context

class IniciarSesion(LoginView):
    template_name = 'Controlador/login.html'
    form_class = LoginForm

class RegistrarView(FormView):
    template_name = 'Controlador/registro.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name='Controlador/home.html'
   