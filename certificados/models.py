from django.db import models
from ej.models import HistoricoMembro


# Create your models here.
class Certificados(models.Model):
    autenticacao = models.CharField(max_length=12)
    historico_membro = models.ForeignKey(HistoricoMembro, on_delete=models.CASCADE, related_name="certificados")