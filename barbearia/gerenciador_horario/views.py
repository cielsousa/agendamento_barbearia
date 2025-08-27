from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DiaDisponivel, HorarioDisponivel, Agendamento, Client, Monday, Tuesday, Wednesday, Thursday, Friday
from .forms import FormAgendamento, ToScheduleMonday
from django.http import HttpResponseRedirect

from django.template.loader import render_to_string

from datetime import date


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


def agendamento(request):
    dias = DiaDisponivel.objects.filter(data__gte=date.today()).order_by('data')[:14]
    return render(request, 'agendamento.html', {'dias': dias})




def horarios_disponiveis(request, dia_id):
    # Recebe a requisição com o dia selecionado, faz a consulta na tabela 
    # de horários de acordo com o dia e retorna os registros de horários
    # disponíveis daquele determinado dia

    horario = HorarioDisponivel.objects.filter(dia=dia_id, agendado=False)

    return JsonResponse([
        {'id': h.id, 'hora': h.hora.strftime('%H:%M')} for h in horario
        ], safe=False)



def form_agendamento(request):
    # Recebe os dados de agendamento do usuário e preenche o formulário de agendamento
    
    dia_id = request.GET.get('dia_id')
    horario_id = request.GET.get('horario_id')

    hora_disponivel = request.GET.get('hora_disponivel')

    form = FormAgendamento(initial={
        'dia_id': dia_id,
        'horario_id': horario_id,
        'hora_disponivel': hora_disponivel
    })

    html = render_to_string("form_agendamento.html", {"form": form}, request)
    return JsonResponse({"html": html})


def agendar(request):
    if request.method == 'POST':
        form = FormAgendamento(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            dia_id = form.cleaned_data['dia_id']
            horario_id = form.cleaned_data['horario_id']
            hora_disponivel = form.cleaned_data['hora_disponivel']

            # Salva o agendamento no horario selecionado pelo cliente
            agendado = Agendamento(cliente=nome,
                                   telefone=telefone,
                                   dia=DiaDisponivel.objects.get(pk=dia_id),
                                   horario=HorarioDisponivel.objects.get(pk=horario_id)
                                   )
            
            agendado.save()

            # Atualiza o registro do horario no banco de dados
            HorarioDisponivel.objects.filter(dia=DiaDisponivel.objects.get(pk=dia_id),
                                            hora=hora_disponivel).update(agendado=True)
            
            return JsonResponse({"success": True, "message": "Agendamento realizado com sucesso!"})

        else:
            html = render_to_string('form_agendamento.html', {'form': form}, request)
            return JsonResponse({'success': False, 'html': html})
    
    

def agendado(request):
    # Filtra o field(dia) da tabela agendamento de acordo com filtro
    # passado no field relacionado(data) da tabela diadisponivel e 
    # retorna os registros correspondentes da tabela agendamento

    dia_agendado = Agendamento.objects.filter( dia__data__gte=date.today()).order_by('dia__data', 'horario__hora')
    dia_agendado_unique = DiaDisponivel.objects.filter(data__gte=date.today()).distinct()[:10]
    context = {
        'dia_agendado': dia_agendado_unique
    }
    return render(request, 'agendado.html', context)



# PROBLEMA NESSA FUÇÃO FDP
def dia_agendado(request, diaId):
   
    horario_agendado = Agendamento.objects.filter(dia=diaId).order_by('dia__data', 'horario__hora')
    
    context = {
        'horario_agendado': horario_agendado
    }

    return JsonResponse([{'horario': h.horario, 'id' : h.id, 'cliente': h.cliente, 'telefone': h.telefone} for h in horario_agendado], safe=False)
    #return render(request, 'agendado.html', context)
