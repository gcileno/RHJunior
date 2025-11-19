from rest_framework import serializers
from .models import Projeto, Tarefas, Escopo

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = '__all__'

class EscopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escopo
        fields = '__all__'
