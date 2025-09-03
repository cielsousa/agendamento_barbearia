from rest_framework import serializers
from .models import HorarioDisponivel, DiaDisponivel, Agendamento

class HorarioDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponivel
        fields = ['id', 'hora']


class DiaDisponivelSerializer(serializers.ModelSerializer):
    horarios = HorarioDisponivelSerializer(many=True, read_only=True)

    class Meta:
        model = DiaDisponivel
        fields = ['id', 'data', 'horarios']

class AgendamentoSerializer(serializers.ModelSerializer):
    dia = DiaDisponivelSerializer(read_only=True)
    horario = HorarioDisponivelSerializer(read_only=True)

    class Meta:
        model = Agendamento
        fields = ['id', 'cliente', 'telefone', 'dia', 'horario', 'criado_em']