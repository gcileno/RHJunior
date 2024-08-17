from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Certificados
from ej.models import HistoricoMembro
import random
import string

def gerar_autenticacao(size=12):
    # Gera uma string aleatória de 12 caracteres
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

@receiver(post_save, sender=HistoricoMembro)
def criar_certificado(sender, instance, created, **kwargs):
    if created:
        # Cria um novo certificado
        certificado = Certificados(
            autenticacao=gerar_autenticacao(),
            historico_membro=instance
        )
        certificado.save()