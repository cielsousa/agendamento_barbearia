from .models import DiaDisponivel, HorarioDisponivel
from datetime import date, timedelta, time, datetime

def gerar_dias(dia, mes):
    # Insere, apartir do dia atual, registros de dias disponíveis
    # até o dia específicado na entrada

    dia_inicial = date.today()
    dia_final = date(2025, mes, dia)

    gerados = 0

    while dia_inicial <= dia_final:

        dia = DiaDisponivel.objects.get_or_create(data=dia_inicial)
        if dia:
            gerados += 1

        dia_inicial += timedelta(days=1)

    print(f'Foram gerados {gerados} dias')

    
def gerar_horario(hora_ini, minuto_ini, hora_fin, minuto_fin):
    # Recebe horário inicial(início do expediente) e horário
    # final(fim do expediente) e popula todos os dias registrados
    # conforme o intervalo de tempo específicado na entrada, sendo 
    # o horário inicial(incluído) acrescido de 30 minutos a cada repetição

    # ------ Implemetar uma maneira de específicar o dia e/ou 
    # intervalo de dias ------

    hora_inicial = time(hora_ini, minuto_ini)
    hora_final = time(hora_fin, minuto_fin)

    dias = DiaDisponivel.objects.all()

    for dia in dias:
        h_criados = 0
        h_existente = 0
        atual = datetime.combine(datetime.today(), hora_inicial)
        final = datetime.combine(datetime.today(), hora_final)
        
        while atual.time() <= final.time():
            criado = HorarioDisponivel.objects.get_or_create(dia=dia, hora=atual.time())
            if criado:
                h_criados += 1
            else:
                h_existente +=1

            atual += timedelta(minutes=30)

    print(f'Horários criados: {h_criados}, Horários existentes: {h_existente}')        

