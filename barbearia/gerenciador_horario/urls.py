from django.urls import path
from . import views

urlpatterns = [
    path('agendado/', views.agendado, name='agendado'),
    path('etc/', views.etc, name='etc'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('api/horarios/<int:dia_id>/', views.horarios_disponiveis, name='horario_disponivel'),
    path('form-agendamento/', views.form_agendamento, name='form-agendamento'),
    path('agendamento/agendar/', views.agendar, name="agendar")
]