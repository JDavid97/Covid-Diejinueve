from django.urls import path
from core.erp.views.paciente.views import *
from core.erp.views.doctor.views import *

app_name = 'erp'

urlpatterns = [
    path('paciente/lista', PacienteListView.as_view(), name='paciente_listar'),
    path('paciente/lista2', lista_paciente, name='paciente_listar2'),
    path('paciente/crear', PacienteCrearView.as_view(), name='paciente_crear'),
    path('paciente/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_editar'),
    path('paciente/borrar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_borrar'),
    
    path('doctor/lista', DoctorListView.as_view(), name='doctor_listar'),
    path('doctor/crear', DoctorCrearView.as_view(), name='doctor_crear'),
    path('doctor/editar/<int:pk>/', DoctorEditView.as_view(), name='doctor_editar'),
    path('doctor/borrar/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_borrar'),
]