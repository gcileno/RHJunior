from django.urls import path
from .views import CertificarViews, EmitirCertificadoView

urlpatterns = [
    path("certificados/emitir/<int:certificado_id>/", EmitirCertificadoView.as_view(), name="emitir_certificado"),
    path('certificados/buscar', CertificarViews.as_view(), name='buscar_certificados'),
]