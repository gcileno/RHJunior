from rest_framework import generics
from .serializers import *
from .models import EmpresasJuinior, Voluntario
from rest_framework.permissions import IsAuthenticated



class JuniorsListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = EmpresasJuinior.objects.all()
    serializer_class = JuniorSerializer

class JuniorsRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = EmpresasJuinior.objects.all()
    serializer_class = JuniorSerializer

class VoluntarioListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

class VoluntarioRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

# Views para Funcao
class FuncaoListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

class FuncaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

# Views para HistoricoMembro
class HistoricoMembroListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = HistoricoMembro.objects.all()
    serializer_class = HistoricoMembroSerializer

class HistoricoMembroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = HistoricoMembro.objects.all()
    serializer_class = HistoricoMembroSerializer

# Views para Departamento
class DepartamentoListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer