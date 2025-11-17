from django.contrib import admin
from .models import Projeto, Escopo, Tarefas

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lider', 'departamento',)
    search_fields = ('nome', 'lider__nome', 'departamento__nome',)

class EscopoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'lider', 'inicio', 'fim',)
    search_fields = ('projeto__nome', 'lider__nome','nome',)

class TarefasAdmin(admin.ModelAdmin):
    list_display = ('escopo',)
    search_fields = ('nome',)
    filter_horizontal = ('assinantes',)

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Escopo, EscopoAdmin)
admin.site.register(Tarefas, TarefasAdmin)