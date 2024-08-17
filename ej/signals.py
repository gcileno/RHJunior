# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Voluntario

@receiver(post_save, sender=Voluntario)
def update_user_info(sender, instance, created, **kwargs):
    if created:
        instance.user_create()
