from django import forms
from .models import *

class FormularioPersona(forms.Form):
    
   nombre_apellido =  forms.CharField(required=True)
   direccion =  forms.CharField(required=True)
   ci =  forms.CharField(required=True)
   salario_total =  forms.CharField(required=True)
   personas_sustento =  forms.CharField(required=True)
