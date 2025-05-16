from django import forms
from django.core.validators import RegexValidator
from .models import Monday, Tuesday, Wednesday, Thursday, Friday
from django.core.exceptions import ValidationError


class AgendamentoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    telefone = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    dia_id = forms.IntegerField(widget=forms.HiddenInput)
    horario_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data


class ToScheduleMonday (forms.Form): 
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Monday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data


class ToScheduleTuesday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Tuesday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data
    

class ToScheduleWednesday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Wednesday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data
    

class ToScheduleThursday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Thursday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data
    

class ToScheduleFriday (forms.Form):
    user_horario = forms.ModelChoiceField(label="Horário desejado:", queryset=Friday.objects.filter(scheduled = False).order_by('horario'))
    user_name = forms.CharField(label="Nome:")
    user_number = forms.CharField(label="Telefone:", validators=[RegexValidator(r'^\d+$', 'Este campo deve conter apenas números.')])
    user_to_schedule = forms.BooleanField(required= False, label="Agendar horário?")

    def clean_user_number(self):
        data = self.cleaned_data["user_number"]
        if not 9 < len(data) < 12:
            raise ValidationError("Número inválido")
        return data
    

class FormFinishAllSchedules (forms.Form):
    form_finish_all_day = forms.BooleanField(widget=forms.CheckboxInput, required=False, label="Deseja finalizar todos os agendamentos?")