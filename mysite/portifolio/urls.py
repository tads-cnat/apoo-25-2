from django.urls import path
from . import views

urlpatterns = [
    path('aluno/cadastrar/', views.AdicaoUsuarioView.as_view(), name='cad_usuario')
]