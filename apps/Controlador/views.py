from django.shortcuts import render
from django.views.generic import TemplateView
import os
# Create your views here.

class IndexView(TemplateView):
    template_name='Controlador/index.html'
    def get_context_data(self,*args,**kwargs):
        l = int(os.environ.get('TIMES'))
        k = int(os.environ.get('DATABASE_URL'))
        context = super().get_context_data(*args,**kwargs)
        context['saludo'] = "Hola"
        context['l'] = l
        context['k'] = k
        
        return context