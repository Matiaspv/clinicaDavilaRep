from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('doctores/', views.DoctorListView.as_view(), name='doctores'),
    path('doctores/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
]