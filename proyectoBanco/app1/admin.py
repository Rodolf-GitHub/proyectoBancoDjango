from django.contrib import admin
from app1.models import *

# Register your models here.
admin.site.register(Banquero)
admin.site.register(Empresa)
admin.site.register(Persona)
admin.site.register(SolicitudCredito)
admin.site.register(SolicitudCreditoEmpresa)
admin.site.register(Usuario)