from django.apps import AppConfig


class EjConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ej'

    def ready(self):
        import ej.signals