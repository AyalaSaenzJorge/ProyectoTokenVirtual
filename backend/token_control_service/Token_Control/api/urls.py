from django.urls import path
from .views import TokensView, TokenValidationView

urlpatterns = [
    path('generar_token', TokensView.as_view(), name='tokens'),
    path('validar_token', TokenValidationView.as_view(), name='token_validation'),
]