from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Client(models.Model):
    name = models.CharField(blank=False, max_length=50)
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.name}, {self.number}'


class Monday(models.Model):
    horario = models.CharField(primary_key=True, max_length=8)
    client_name = models.CharField(max_length=40)
    client_number = models.CharField(max_length=11)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.horario
    

class Tuesday(models.Model):
    horario = models.CharField(max_length=8)
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    client_number = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    scheduled = models.BooleanField(default=False)

class Wednesday(models.Model):
    horario = models.CharField(max_length=8)
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    client_number = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    scheduled = models.BooleanField(default=False)

class Thursday(models.Model):
    horario = models.CharField(max_length=8)
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    client_number = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    scheduled = models.BooleanField(default=False)

class Friday(models.Model):
    horario = models.CharField(max_length=8)
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    client_number = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='+')
    scheduled = models.BooleanField(default=False)
