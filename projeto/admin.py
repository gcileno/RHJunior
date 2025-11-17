from django.contrib import admin
from .models import Projeto, Escopo, Tarefas

# Register your models here.
admin.site.register(Projeto)
admin.site.register(Escopo)
admin.site.register(Tarefas)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lider', 'departamento',)
    search_fields = ('nome', 'lider__nome', 'departamento__nome',)