from django.urls import path
from .views import CertificarViews

urlpatterns = [
    path('certificados/buscar', CertificarViews.as_view(), name='buscar_certificados'),
]