from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .models import Monday, Tuesday, Wednesday, Thursday, Friday

class ToScheduleMonday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Monday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

class ToScheduleTuesday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Tuesday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

class ToScheduleWednesday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Wednesday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

class ToScheduleThursday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Thursday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

class ToScheduleFriday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Friday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

"""
class ToScheduleMonday(ModelForm):
    class Meta:
        model = Monday
        fields = '__all__' 
"""