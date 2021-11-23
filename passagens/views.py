from rest_framework import viewsets, filters
from passagens.models import Voo, Status, Clientes
from passagens.serializers import VooSerializer, StatusSerializer, ClientesSerializer

class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','numero_do_voo']

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','status']

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','primeiro_nome','sobrenome']