from django.urls import path
from .views import (
    ProjetoListView
)

urlpatterns = [
    path('projetos/', ProjetoListView.as_view(), name='projeto-list'),
]