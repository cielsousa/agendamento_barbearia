from django.urls import path
from . import views

urlpatterns = [
    path('horario', views.horario, name='horario'),
    path('horario/segunda/', views.monday, name='monday'),
    path('horario/terca/', views.tuesday, name='tuesday'),
    path('horario/segunda/segundaAgendado/', views.segundaAgendado, name='segundaAgendado'),
    #path('horario/segunda/tercaAgendado/', views.tercaAgendado, name='tercaAgendado')
    #path('horario/segunda/segundaAgendado/', views.segundaAgendado, name='segundaAgendado')
    #path('horario/segunda/segundaAgendado/', views.segundaAgendado, name='segundaAgendado')
    #path('horario/segunda/segundaAgendado/', views.segundaAgendado, name='segundaAgendado')

]