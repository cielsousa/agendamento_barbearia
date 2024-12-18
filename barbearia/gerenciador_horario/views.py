from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Monday, Tuesday, Wednesday, Thursday, Friday
from .forms import ToScheduleMonday, ToScheduleTuesday, ToScheduleWednesday, ToScheduleThursday, ToScheduleFriday
from django.http import HttpResponseRedirect


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
    context = {'form': ToScheduleMonday}

    return render(request, 'segunda.html', context=context)


def mondaySchedule(request):
    
    #Monday_instance = get_object_or_404(Monday)

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
        return render(request, 'segunda.html', {'form': form})


def tuesday(request):
    context = {'form': ToScheduleTuesday}

    return render(request, 'terca.html', context)


def tuesdaySchedule(request):
    
    #Monday_instance = get_object_or_404(Monday)

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

            return HttpResponseRedirect("")
    
        else:
            return render(request, 'tercaAgendado.html', {'form': form})

    else:
        form = ToScheduleTuesday()
        return render(request, 'tercaAgendado.html', {'form': form})


def wednesday(request):
    context = {'form': ToScheduleWednesday}

    return render(request, 'quarta.html', context)


def wednesdaySchedule(request):
    
    #Monday_instance = get_object_or_404(Monday)

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

            return HttpResponseRedirect("")
    
        else:
            return render(request, 'wednesdayAgendado.html', {'form': form})

    else:
        form = ToScheduleWednesday()
        return render(request, 'wednesdayAgendado.html', {'form': form})


def thursday(request):
    context = {'form': ToScheduleThursday}

    return render(request, 'quinta.html', context)


def thursdaySchedule(request):
    
    #Monday_instance = get_object_or_404(Monday)

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

            return HttpResponseRedirect("")
    
        else:
            return render(request, 'thursdayAgendado.html', {'form': form})

    else:
        form = ToScheduleThursday()
        return render(request, 'thursdayAgendado.html', {'form': form})


def friday(request):
    context = {'form': ToScheduleFriday}

    return render(request, 'sexta.html', context)

def fridaySchedule(request):
    
    #Monday_instance = get_object_or_404(Monday)

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

            return HttpResponseRedirect("")
    
        else:
            return render(request, 'sextaAgendado.html', {'form': form})

    else:
        form = ToScheduleFriday()
        return render(request, 'sextaAgendado.html', {'form': form})

def timeScheduled(request):

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
    
    return render(request, 'agendado.html', context)