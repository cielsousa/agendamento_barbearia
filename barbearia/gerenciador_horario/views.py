from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import DiaDisponivel, HorarioDisponivel, Agendamento, Client, Monday, Tuesday, Wednesday, Thursday, Friday
from .forms import ToScheduleMonday, ToScheduleTuesday, ToScheduleWednesday, ToScheduleThursday, ToScheduleFriday, FormFinishAllSchedules, AgendamentoForm
from django.http import HttpResponseRedirect
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib import messages

from django.template.loader import render_to_string

from datetime import date
import json


def horario(request):
    table_monday = Monday.objects.all().order_by('horario')
    table_tuesday = Tuesday.objects.all().order_by('horario')
    table_wednesday = Wednesday.objects.all().order_by('horario')
    table_thursday = Thursday.objects.all().order_by('horario')
    table_friday = Friday.objects.all().order_by('horario')


    context = {
        'table_monday': table_monday,
        'table_tuesday': table_tuesday,
        'table_wednesday': table_wednesday,
        'table_thursday': table_thursday,
        'table_friday': table_friday,
    }

    return render(request, 'horario.html', context=context)


def etc(request):
 
    return render(request, 'etc.html')


def monday(request):
    if request.method == "POST":
        form = ToScheduleMonday(request.POST)

        #check if the data is valid
        if form.is_valid():
            form_user_horario = form.cleaned_data['user_horario']
            form_user_name = form.cleaned_data['user_name']
            form_user_number = form.cleaned_data['user_number']
            
            if  form.cleaned_data['user_to_schedule'] == False:
                user_scheduled = False
            else:
                user_scheduled = True
            
            
            #form_user_horario = request.POST['user_horario']
            #form_user_name = request.POST['user_name']
            #form_user_number = request.POST['user_number']
            #form_user_to_schedule = request.POST['user_to_schedule']

            # Se o horario escolhido estiver dispinível,
            # cria uma nova instância do horário escolhido na semana
         
            agendamento = Monday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
            
            agendamento.save()

            return HttpResponseRedirect('/')
        
        else:
            return render(request, 'segunda.html', {'form': form})
        
    else:
        form = ToScheduleMonday()
        context = {'form': form}
        return render(request, 'segunda.html', context)


def tuesday(request):
    if request.method == "POST":
        form = ToScheduleTuesday(request.POST)

        #check if the data is valid
        if form.is_valid():
            form_user_horario = form.cleaned_data['user_horario']
            form_user_name = form.cleaned_data['user_name']
            form_user_number = form.cleaned_data['user_number']
            
            if  form.cleaned_data['user_to_schedule'] == False:
                user_scheduled = False
            else:
                user_scheduled = True
            
            
            #form_user_horario = request.POST['user_horario']
            #form_user_name = request.POST['user_name']
            #form_user_number = request.POST['user_number']
            #form_user_to_schedule = request.POST['user_to_schedule']

            # Se o horario escolhido estiver dispinível,
            # cria uma nova instância do horário escolhido na semana
         
            agendamento = Tuesday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
                
            agendamento.save()

            return HttpResponseRedirect("/")
    
        else:
            return render(request, 'terca.html', {'form': form})

    else:
        context = {'form': ToScheduleTuesday}
        return render(request, 'terca.html', context)


def wednesday(request):
    if request.method == "POST":
        form = ToScheduleWednesday(request.POST)

        #check if the data is valid
        if form.is_valid():
            form_user_horario = form.cleaned_data['user_horario']
            form_user_name = form.cleaned_data['user_name']
            form_user_number = form.cleaned_data['user_number']
            
            if  form.cleaned_data['user_to_schedule'] == False:
                user_scheduled = False
            else:
                user_scheduled = True
            
            
            #form_user_horario = request.POST['user_horario']
            #form_user_name = request.POST['user_name']
            #form_user_number = request.POST['user_number']
            #form_user_to_schedule = request.POST['user_to_schedule']

            # Se o horario escolhido estiver dispinível,
            # cria uma nova instância do horário escolhido na semana
         
            agendamento = Wednesday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
                
            agendamento.save()

            return HttpResponseRedirect("/")
    
        else:
            return render(request, 'quarta.html', {'form': form})

    else:
        context = {'form': ToScheduleWednesday}
        return render(request, 'quarta.html', context)


def thursday(request):
    if request.method == "POST":
        form = ToScheduleThursday(request.POST)

        #check if the data is valid
        if form.is_valid():
            form_user_horario = form.cleaned_data['user_horario']
            form_user_name = form.cleaned_data['user_name']
            form_user_number = form.cleaned_data['user_number']
            
            if  form.cleaned_data['user_to_schedule'] == False:
                user_scheduled = False
            else:
                user_scheduled = True 
            
            
            #form_user_horario = request.POST['user_horario']
            #form_user_name = request.POST['user_name']
            #form_user_number = request.POST['user_number']
            #form_user_to_schedule = request.POST['user_to_schedule']

            # Se o horario escolhido estiver dispinível,
            # cria uma nova instância do horário escolhido na semana
         
            agendamento = Thursday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
                
            agendamento.save()

            return HttpResponseRedirect("/")
    
        else:
            return render(request, 'quinta.html', {'form': form})

    else:
        context = {'form': ToScheduleThursday}
        return render(request, 'quinta.html', context)


def friday(request):
    if request.method == "POST":
        form = ToScheduleFriday(request.POST)

        #check if the data is valid
        if form.is_valid():
            form_user_horario = form.cleaned_data['user_horario']
            form_user_name = form.cleaned_data['user_name']
            form_user_number = form.cleaned_data['user_number']
            
            if  form.cleaned_data['user_to_schedule'] == False:
                user_scheduled = False
            else:
                user_scheduled = True
            
            
            #form_user_horario = request.POST['user_horario']
            #form_user_name = request.POST['user_name']
            #form_user_number = request.POST['user_number']
            #form_user_to_schedule = request.POST['user_to_schedule']

            # Se o horario escolhido estiver dispinível,
            # cria uma nova instância do horário escolhido na semana
         
            agendamento = Friday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
                
            agendamento.save()

            return HttpResponseRedirect("/")
    
        else:
            return render(request, 'sexta.html', {'form': form})

    else:
        context = {'form': ToScheduleFriday}
        return render(request, 'sexta.html', context)


def timeScheduled(request):

    table_monday = Monday.objects.all().order_by('horario')
    table_tuesday = Tuesday.objects.all().order_by('horario')
    table_wednesday = Wednesday.objects.all().order_by('horario')
    table_thursday = Thursday.objects.all().order_by('horario')
    table_friday = Friday.objects.all().order_by('horario')

    monday_schedule = Monday.objects.all().filter(scheduled=True)
    tuesday_schedule = Tuesday.objects.all().filter(scheduled=True)
    wednesday_schedule = Wednesday.objects.all().filter(scheduled=True)
    thursday_schedule = Thursday.objects.all().filter(scheduled=True)
    friday_schedule = Friday.objects.all().filter(scheduled=True)
    
    context = {
        'table_monday': table_monday,
        'table_tuesday': table_tuesday,
        'table_wednesday': table_wednesday,
        'table_thursday': table_thursday,
        'table_friday': table_friday,

        'monday_schedule': monday_schedule,
        'tuesday_schedule': tuesday_schedule,
        'wednesday_schedule': wednesday_schedule,
        'thursday_schedule': thursday_schedule,
        'friday_schedule': friday_schedule,
        'form': FormFinishAllSchedules
    }
    
    return render(request, 'agendado.html', context)


def mondaySchedule(request):
        
        monday_schedule = Monday.objects.all()

        if request.method == 'POST':
            form = FormFinishAllSchedules(request.POST)

            #finish_all_day = form["form_finish_all_day"]
            
            # CONSERTAR ESSE BLOCO, ESTÁ CAINDO SEMPRE NO ELSE

            for horario in monday_schedule:
                horario.scheduled = False
                horario.save()

        return HttpResponseRedirect('/agendado/')


def tuesdaySchedule(request):
        
        tuesday_schedule = Tuesday.objects.all()

        if request.method == 'POST':
            form = FormFinishAllSchedules(request.POST)

            #finish_all_day = form["form_finish_all_day"]
            
            # CONSERTAR ESSE BLOCO, ESTÁ CAINDO SEMPRE NO ELSE

            for horario in tuesday_schedule:
                horario.scheduled = False
                horario.save()

        return HttpResponseRedirect('/agendado/')


def wednesdaySchedule(request):
        
        wednesday_schedule = Wednesday.objects.all()

        if request.method == 'POST':
            form = FormFinishAllSchedules(request.POST)

            #finish_all_day = form["form_finish_all_day"]
            
            # CONSERTAR ESSE BLOCO, ESTÁ CAINDO SEMPRE NO ELSE

            for horario in wednesday_schedule:
                horario.scheduled = False
                horario.save()

        return HttpResponseRedirect('/agendado/')


def thursdaySchedule(request):
        
        thursday_schedule = Thursday.objects.all()

        if request.method == 'POST':
            form = FormFinishAllSchedules(request.POST)

            #finish_all_day = form["form_finish_all_day"]
            
            # CONSERTAR ESSE BLOCO, ESTÁ CAINDO SEMPRE NO ELSE

            for horario in thursday_schedule:
                horario.scheduled = False
                horario.save()

        return HttpResponseRedirect('/agendado/')


def fridaySchedule(request):
        
        friday_schedule = Friday.objects.all()

        if request.method == 'POST':
            form = FormFinishAllSchedules(request.POST)

            #finish_all_day = form["form_finish_all_day"]
            
            # CONSERTAR ESSE BLOCO, ESTÁ CAINDO SEMPRE NO ELSE

            for horario in friday_schedule:
                horario.scheduled = False
                horario.save()

        return HttpResponseRedirect('/agendado/')


def agendamento_view(request):
    dias = DiaDisponivel.objects.filter(data__gte=date.today()).order_by('data')[:14]
    return render(request, 'agendamento.html', {'dias': dias})


def horarios_disponiveis(request, dia_id):
    horarios = HorarioDisponivel.objects.filter(dia_id=dia_id)

    return JsonResponse([
        {'id': h.id, 'hora': h.hora.strftime('%H:%M')} for h in horarios
        ], safe=False)


def criar_agendamento(request):
    dias = DiaDisponivel.objects.all().order_by('data')[:7]

    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            dia_id = form.cleaned_data['dia_id']
            horario_id = form.cleaned_data['horario_id']

        if Agendamento.objects.filter(dia_id=dia_id, horario_id=horario_id).exists():
            messages.error(request, {'Horário já foi agendado'})
        else:
            cliente, _ = Client.objects.get_or_create(name=nome, number=telefone)

            Agendamento.objects.create(
                cliente=cliente,
                dia_id=dia_id,
                horario_id=horario_id
            )
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('agendamento')
        
    else:
        form = AgendamentoForm()

    context = {
        'dias': dias,
        'form': form
        }
    
    return JsonResponse(context, safe=False)





def form_agendamento(request):
    dia_id = request.GET.get('dia_id')
    horario_id = request.GET.get('horario_id')

    form = AgendamentoForm(initial={
        'dia_id': dia_id,
        'horario_id': horario_id
    })

    html = render_to_string("form_agendamento.html", {"form": form}, request)
    return JsonResponse({"html": html})
