from django.contrib import admin
from .models import EmpresasJuinior, HistoricoMembro, Funcao, Departamento, Voluntario, Informacoes, AnaliseDesempenho

# Consultas e filtros em ADMIN
class EmpresasJuiniorAdmin(admin.ModelAdmin):
    list_display=('razao_social',)
    search_fields = ('razao_social','cnpj',)

class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula',)
    search_fields = ('nome', 'ies', 'cpf',)

class HistoricoMembroAdmin(admin.ModelAdmin):
    list_display = ('voluntario',)
    search_fields = ('voluntario',)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class FuncaoAdmim(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DesempenhoAdmin(admin.ModelAdmin):
    list_display = ('voluntario',)
    search_fields = ('voluntario',)

admin.site.register(EmpresasJuinior, EmpresasJuiniorAdmin)
admin.site.register(Funcao, FuncaoAdmim)
admin.site.register(HistoricoMembro, HistoricoMembroAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Informacoes)
admin.site.register(AnaliseDesempenho)