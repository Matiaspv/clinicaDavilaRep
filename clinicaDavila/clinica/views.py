from django.shortcuts import render
from .models import Doctor, Especialidad
from django.views import generic
# Create your views here.


def index(request):

    num_Doctors = Doctor.objects.all().count()
    num_Especiality = Especialidad.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    num_visits=request.session['num_visits']=num_visits+1


    num_EspecialityNeuro = Especialidad.objects.filter(name='Neurocirujano').count()
    
    return render(
        request,
            'index.html',
            context={'num_doctors':num_Doctors,'num_especiality':num_Especiality,'num_especialityneuro': num_EspecialityNeuro}
            context={'num_doctors':num_Doctors,'num_instances':num_instances,'num_instances_available':num_instances_available,
            'num_especiality':num_especiality,'num_visits':num_visits},
    )


class DoctorDetailView(generic.ListView):
    model = Doctor

class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 10

    def get_context_data(self, **kwargs):

        context = super(DoctorListView, self).get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'
        

        return context



    
    


