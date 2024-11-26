from django.urls import path
from . import views

urlpatterns = [
    path('horario', views.horario, name='horario'),
    path('horario/segunda/', views.monday, name='monday'),
    path('horario/terca/', views.tuesday, name='tuesday'),
    path('horario/quarta/', views.wednesday, name='wednesday'),
    path('horario/quinta/', views.thursday, name='thursday'),
    path('horario/sexta/', views.friday, name='friday'),
    path('horario/segunda/segundaAgendado/', views.mondaySchedule, name='mondaySchedule'),
    #path('horario/terca/tercaAgendado/', views.tercaAgendado, name='tercaAgendado')
    #path('horario/quarta/quartaAgendado/', views.quartaAgendado, name='quartaAgendado')
    #path('horario/quinta/quintaAgendado/', views.quintaAgendado, name='quintaAgendado')
    #path('horario/sexta/sextaAgendado/', views.sextaAgendado, name='sextaAgendado')

]