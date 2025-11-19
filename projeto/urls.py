from django.urls import path
from .views import (
    ProjetoListView, ProjetoDetailView
)

urlpatterns = [
    path('projetos/', ProjetoListView.as_view(), name='projeto-list'),
    path('projetos/<int:pk>/', ProjetoDetailView.as_view(), name='projeto-detail'),
]