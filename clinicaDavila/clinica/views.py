from django.shortcuts import render
from .models import Doctor, Especialidad
from django.views import generic
# Create your views here.

def index(request):

    
    
    return render(
        request,
            'index.html',
            
    )

def listadoME(request):

    num_Doctors = Doctor.objects.all().count()

    num_Especiality = Especialidad.objects.all().count()


    num_EspecialityNeuro = Especialidad.objects.filter(name='Neurocirujano').count()
    
    return render(
        request,
            'doctor_list.html',
            context={'num_doctors':num_Doctors,'num_especiality':num_Especiality,'num_especialityneuro': num_EspecialityNeuro}
    )

class DoctorListadoView(generic.ListView):
    model = Doctor