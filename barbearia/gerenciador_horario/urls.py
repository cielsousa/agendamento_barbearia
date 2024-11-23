from django.urls import path
from . import views

urlpatterns = [
    path('horario', views.horario, name='horario'),
    path('horario/segunda/', views.monday, name='monday'),
    path('horario/segunda/segundaAgendado/', views.segundaAgendado, name='segundaAgendado')
]