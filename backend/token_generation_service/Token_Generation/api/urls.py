from django.urls import path
from .views import TokenGenerationView

urlpatterns = [
    path('crear_token', TokenGenerationView.as_view(), name='crear_token')
]