from django.db import models


# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    edad = models.IntegerField()  # Edad en años
    meses = models.IntegerField()  # Meses parcial
    dias = models.IntegerField()  # Dias parcial
    fecha_nacimiento = models.DateTimeField()  # Fecha de nacimiento
    fecha_rescate = models.DateTimeField()  # Fecha cuando se rescato al perro
    sexo = models.IntegerField()
    tamanio = models.ForeignKey('Tamanio')
    tipo_pelaje = models.ForeignKey('TipoPelaje')
    nivel_actividad = models.ForeignKey('NivelActividad')


class Tamanio(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.IntegerField()


class TipoPelaje(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()


class NivelActividad(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
