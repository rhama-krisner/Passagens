from django.db import models
from datetime import date
import datetime
from random import randint
# Create your models here.

class Status(models.Model):
    STATUS = (
        ("ABERTO","ABERTO"),
        ("PAGO","PAGO"),
        ("CANCELADO","CANCELADO")
    )
    date = datetime.date.today()

    id = models.AutoField(primary_key=True, serialize=True, verbose_name='ID')
    status = models.CharField(max_length=10, choices=STATUS, blank=False, null=False, default='ABERTO')
    criado = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.status

class Clientes(models.Model):
    id = models.AutoField(primary_key=True, serialize=True, verbose_name='ID')
    primeiro_nome = models.CharField(max_length=255, blank=False, null=False)
    sobrenome = models.CharField(max_length=255, blank=False, null=False)
    status_compra = models.ForeignKey(Status, related_name='cliente', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.primeiro_nome

class Voo(models.Model):

    COMPANHIAS = (
        ("AEROLINEAS","AEROLINEAS"),
        ("AZUL","AZUL"),
        ("COPA AIRLINES","COPA AIRLINES"),
        ("GOL","GOL"),
        ("LATAM", "LATAM"),
        ("MAYAIR","MAYAIR"),
        ("PASSAREDO","PASSAREDO"),
        ("SURINAM","SURINAM"),
        ("TAP","TAP"),
    )

    
    id = models.AutoField(primary_key=True, serialize=True, verbose_name='ID')
    numero_do_voo = models.IntegerField(blank=False, null=False)
    preco = models.IntegerField(blank=False, null=False)
    data_ida = models.DateField(blank=False, null=False)
    companhia_ida = models.CharField(max_length=20, choices=COMPANHIAS,blank=False, null=False)
    data_volta = models.DateField(blank=False, null=False)
    companhia_volta = models.CharField(max_length=20, choices=COMPANHIAS, blank=False, null=False)
    criado = models.DateTimeField(auto_now_add=True, blank=True)
    passageiro = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='Clientes', blank=True)

    def __str__(self):
        return self.numero_do_voo



    
