from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=20, primary_key=True)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_usuario

class Banquero(models.Model):
    rol = models.CharField(max_length=20)
    nombre_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.nombre_usuario.nombre_usuario

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=20)
    nombre_director = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    ganancia_anual = models.IntegerField()
    cantidad_trabajadores = models.IntegerField()
    ministerio = models.CharField(max_length=20)
    codigo = models.CharField(max_length=11)
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_empresa

class Persona(models.Model):
    nombre_apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    carnet_identidad = models.CharField(max_length=11)
    salario_total = models.IntegerField()
    personas_sustento = models.IntegerField()
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_apellido

class SolicitudCredito(models.Model):
    valor = models.IntegerField()
    estado = models.CharField(max_length=20)
    id_solicitud_credito = models.AutoField(primary_key=True)
    nombre_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class SolicitudCreditoEmpresa(models.Model):
    nombre_solicitante = models.CharField(max_length=20)
    direccion_solicitante = models.CharField(max_length=50)
    id_solicitud_credito_empresa = models.AutoField(primary_key=True)
    solicitud_credito_id_solicitud_credito = models.ForeignKey(SolicitudCredito, on_delete=models.CASCADE)

class Meta:
        managed=False
        db_table='solicitud_credito_empresa'

