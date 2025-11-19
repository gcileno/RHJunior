from rest_framework import generics
from .serializer import EscopoSerializer, ProjetoSerializer, TarefasSerializer
from .models import Projeto, Tarefas, Escopo
from rest_framework.permissions import IsAuthenticated

class ProjetoListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, ) # Descomente esta linha para exigir autenticação
    serializer_class = ProjetoSerializer

    def get_queryset(self):
        user = self.request.user

        # Se for admin, retorna todos os projetos
        if user.is_staff or user.is_superuser:
            return Projeto.objects.all()
        
        # Caso contrário, retorna apenas os projetos que o usuário participa
        return Projeto.objects.filter(membros=user.voluntario)