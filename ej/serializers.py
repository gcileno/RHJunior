from rest_framework import serializers
from .models import EmpresasJuinior, Voluntario,Funcao, HistoricoMembro, Departamento

class JuniorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasJuinior
        fields = '__all__'

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = '__all__'

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

class HistoricoMembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoMembro
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'