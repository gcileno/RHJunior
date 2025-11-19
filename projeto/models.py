from django.db import models
from ej.models import Voluntario, Departamento

#TODO Verificar __str__ em relação a herança
class BaseModel(models.Model):

    class StatusChoices(models.TextChoices):
        PENDENTE = "Pendente", "Pendente"
        DESENVOLVIMENTO = "Desenvolvimento", "Desenvolvimento"
        TESTE = "Teste", "Teste"
        DEBUG = "Debug", "Debug"
        CONCLUIDO = "Concluído", "Concluído"

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    inicio= models.DateTimeField(null=True, blank=True)
    fim = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDENTE,
    )
    class Meta:
        abstract = True
    

class Projeto(BaseModel):

    lider = models.ForeignKey(
        Voluntario, 
        on_delete=models.CASCADE, 
        related_name="projetos_liderados",
        blank=True, 
        null=True
        )
    
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name="projetos",
        blank=True,
        null=True
        )
    
    membros = models.ManyToManyField(
        Voluntario,
        related_name="projetos",
        blank=True
        )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Escopo(BaseModel):
    projeto = models.ForeignKey(
        "Projeto",
        on_delete=models.CASCADE,
        related_name="objetivos"
        )
    
    lider = models.ForeignKey(
        Voluntario,
        on_delete=models.CASCADE, 
        related_name="escopos_liderados",
    )


    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Escopo"
        verbose_name_plural = "Escopos"

class Tarefas(BaseModel):
    escopo = models.ForeignKey(
        "Escopo", # Aqui eu vou me relacionar com a classe filha de projeto
        on_delete=models.CASCADE,
        related_name="atividades"
        )

    assinantes = models.ManyToManyField(
        Voluntario,
        related_name="atividades_assinadas",
        blank=True
        )
    
    def __str__(self):
        return f"{self.nome} - {self.inicio} - {self.fim}"
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
