from django.urls import path
from . import views

urlpatterns = [
    path('', views.horario, name='horario'),
    path('segunda/', views.monday, name='monday'),
    path('terca/', views.tuesday, name='tuesday'),
    path('quarta/', views.wednesday, name='wednesday'),
    path('quinta/', views.thursday, name='thursday'),
    path('sexta/', views.friday, name='friday'),

    path('agendado/segundaAgendado/', views.mondaySchedule, name='mondaySchedule'),
    path('agendado/tercaAgendado/', views.tuesdaySchedule, name='tuesdaySchedule'),
    path('agendado/quartaAgendado/', views.wednesdaySchedule, name='wednesdaySchedule'),
    path('agendado/quintaAgendado/', views.thursdaySchedule, name='thursdaySchedule'),
    path('agendado/sextaAgendado/', views.fridaySchedule, name='fridaySchedule'),

    path('agendado/', views.timeScheduled, name='timeScheduled'),
    path('etc', views.etc, name='etc')
]