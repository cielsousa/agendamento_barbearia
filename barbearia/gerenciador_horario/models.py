from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
import time

# Create your models here.


class Client(models.Model):
    name = models.CharField(blank=False, max_length=50)
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.name}, {self.number}'


class DiaDisponivel(models.Model):
    data = models.DateField(unique=True)

    def __str__(self):
        return f'{self.data.strftime('%d/%m/%Y')}'
    

class HorarioDisponivel(models.Model):
    dia = models.ForeignKey(DiaDisponivel, on_delete=models.CASCADE, related_name='horarios')
    hora = models.TimeField()
    agendado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.hora.strftime('%H:%M')}'
    

class Agendamento(models.Model):
    cliente = models.CharField(max_length=20)
    telefone = models.IntegerField(default=11111111111)
    dia = models.ForeignKey(DiaDisponivel, on_delete=models.CASCADE, related_name='dia_disponivel')
    horario = models.ForeignKey(HorarioDisponivel, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('dia', 'horario')



class Monday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.horario
    

class Tuesday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.horario

class Wednesday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)


    def __str__(self):
        return self.horario
    

class Thursday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.horario

class Friday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.horario
