from django.db import models
from  django.urls import reverse
import uuid
# Create your models here.

class Especialidad(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Doctor(models.Model):

    rut = models.IntegerField(primary_key=True, help_text='Rut unico del doctors')
    dv = models.CharField(max_length=1, default='0')
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    especialidad = models.ForeignKey('Especialidad', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['nombre' , 'apellido']

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.rut)])

    def __str__(self):
        return f'{self.rut}, {self.nombre}, ({self.especialidad.name})'