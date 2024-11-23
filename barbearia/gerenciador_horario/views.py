from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Monday, Tuesday, Wednesday, Thursday, Friday
from .forms import ToSchedule
from django.http import HttpResponseRedirect
#from .forms import ToScheduleMonday

# Create your views here.


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

def monday(request):
    context = {
        'form': ToSchedule,
        #'formModel': ToScheduleMonday
    }

    return render(request, 'segunda.html', context=context)



def segundaAgendado(request):
    
    #Monday_instance = get_object_or_404(Monday)

    if request.method == "POST":
        form = ToSchedule(request.POST)

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

            # Cria uma nova instância do horário escolhido na semana
            agendamento = Monday(horario=form_user_horario,
                                client_name= form_user_name,
                                client_number= form_user_number,
                                scheduled= user_scheduled)
            
            agendamento.save()

            return HttpResponseRedirect("/barbearia/horario")
        
    else:
        form = ToSchedule()

    return render(request, 'segundaAgendado.html', {'form': form})
