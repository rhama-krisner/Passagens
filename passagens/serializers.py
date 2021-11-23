from rest_framework import serializers
from passagens.models import Voo, Status, Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = [
            'id',
            'primeiro_nome',
            'sobrenome',
            'status_compra',
        ]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','status','criado']

class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = [
            'id',
            'numero_do_voo',
            'preco',
            'data_ida',
            'companhia_ida',
            'data_volta',
            'companhia_volta',
            'criado',
            'passageiro'
        ]


