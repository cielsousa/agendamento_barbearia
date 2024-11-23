from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
#from django.forms import ModelForm
#from .models import Monday

class ToSchedule (forms.Form):
    user_horario = forms.CharField(label="Horario:")
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    
"""
class ToScheduleMonday(ModelForm):
    class Meta:
        model = Monday
        fields = '__all__' 
"""