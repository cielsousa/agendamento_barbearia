from django.urls import path
from . import views

urlpatterns = [
    path('', views.horario, name='horario'),
    path('segunda/', views.monday, name='monday'),
    path('terca/', views.tuesday, name='tuesday'),
    path('quarta/', views.wednesday, name='wednesday'),
    path('quinta/', views.thursday, name='thursday'),
    path('sexta/', views.friday, name='friday'),
    path('segunda/segundaAgendado/', views.mondaySchedule, name='mondaySchedule'),
    path('terca/tercaAgendado/', views.tuesdaySchedule, name='tuesdaySchedule'),
    path('quarta/quartaAgendado/', views.wednesdaySchedule, name='wednesdaySchedule'),
    path('quinta/quintaAgendado/', views.thursdaySchedule, name='thursdaySchedule'),
    path('sexta/sextaAgendado/', views.fridaySchedule, name='fridaySchedule'),
    path('agendado/', views.timeScheduled, name='timeScheduled'),
    path('etc', views.etc, name='etc')
]