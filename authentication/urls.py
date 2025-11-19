from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # rota para obter access + refresh token
    path("authentication/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # rota para renovar o access token usando o refresh
    path("authentication/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
