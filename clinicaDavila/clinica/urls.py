from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('doctores/', views.DoctorListadoView.as_view(), name='listadoME'),
]