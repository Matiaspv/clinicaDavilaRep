from django.db import models
from  django.urls import reverse
import uuid
# Create your models here.

class Especialidad(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Doctor(models.Model):

    rut = models.UUIDField(primary_key=True, help_text='Rut unico del doctors')
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    especialidad = models.ForeignKey('Especialidad', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.rut}, {self.nombre}, ({self.especialidad.name})'


