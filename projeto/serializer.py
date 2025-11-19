from rest_framework import serializers
from .models import Projeto, Tarefas, Escopo

class ProjetoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projeto
        fields = '__all__'

class TarefasSerializer(serializers.ModelSerializer):
    escopo = serializers.PrimaryKeyRelatedField(queryset=Escopo.objects.all())
    class Meta:
        model = Tarefas
        fields = '__all__'

class EscopoSerializer(serializers.ModelSerializer):
    tarefas = TarefasSerializer(many=True, read_only=True)
    class Meta:
        model = Escopo
        fields = '__all__'
