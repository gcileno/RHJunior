from django.contrib import admin
from .models import Certificados

# Register your models here.
class CertificadosAdmin(admin.ModelAdmin):
    list_display=('autenticacao',)
    search_fields = ('autenticacao','historico_membro',)

admin.site.register( Certificados, CertificadosAdmin)