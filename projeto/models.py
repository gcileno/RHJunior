from django.db import models
from ej.models import Voluntario, Departamento


class Projeto(models.Model):

    lider = models.ForeignKey(
        "Voluntario", 
        on_delete=models.CASCADE, 
        related_name="projetos_liderados",
        blank=True, 
        null=True
        )
    
    departamento = models.ForeignKey(
        "Departamento",
        on_delete=models.CASCADE,
        related_name="projetos",
        blank=True,
        null=True
        )
    
    membross = models.ManyToManyField(
        "Voluntario")
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.BooleanField(verbose_name="Status", default=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Requisitos(models.Model):
    """
    Essa classe deve respesentar os objetivos gerais do projeteto,
    representando em um contexto geral ouqe se pretenden alcançar com sua execução.
    deve ser dividido em diversas atividades específicas.
    Ex: 
        Objetivo Geral: Criar Tela de login
        Atividades:
            - Criar layout da tela
            - Implementar validação de dados
            - Testar funcionalidade 
    """
    projeto = models.ForeignKey(
        "Projeto",
        on_delete=models.CASCADE,
        related_name="objetivos"
        )
    
    lider = models.ForeignKey(
        "Voluntario", 
        related_name="objetivos_liderados",
    )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

class Tarefas(models.Model):
    projeto = models.ForeignKey(
        "Requisitos", # Aqui eu vou me relacionar com a classe filha de projeto
        on_delete=models.CASCADE,
        related_name="atividades"
        )
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    assinantes = models.ManyToManyField(
        "Voluntario",
        related_name="atividades_assinadas",
        blank=True
        )
    def __str__(self):
        return f"{self.titulo} - {self.projeto.nome}"
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
