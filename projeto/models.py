from django.db import models
from ej.models import Voluntario, Departamento

class BaseModel(models.Model):

    class StatusChoices(models.TextChoices):
        PENDENTE = "Pendente", "Pendente"
        DESENVOLVIMENTO = "Desenvolvimento", "Desenvolvimento"
        DEBUG = "Debug", "Debug"
        CONCLUIDO = "Concluído", "Concluído"

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    inicio= models.DateTimeField(auto_now_add=True)
    fim = models.DateTimeField(auto_now=True)

    _status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDENTE,
    )
    class Meta:
        abstract = True
    

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

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Escopo(models.Model):
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

    def __str__(self):
        return f"{self.projeto.nome} - {self.lider.nome}"
    
    class Meta:
        verbose_name = "Escopo"
        verbose_name_plural = "Escopos"

class Tarefas(models.Model):
    projeto = models.ForeignKey(
        "Escopo", # Aqui eu vou me relacionar com a classe filha de projeto
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
    
    status = models.BooleanField(verbose_name="Concluída", default=False)

    def __str__(self):
        return f"{self.titulo} - {self.projeto.nome}"
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
