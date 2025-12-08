from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='portifolio/index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='portifolio/login.html'), name='login'),
    path('aluno/cadastrar/', views.AdicaoUsuarioView.as_view(), name='cad_usuario'),
    path('vaga/<int:id_vaga>/comentar/', views.ComentarVagaView.as_view(), name='comenta_vaga'),
    path('vagas/buscar/', views.PesquisaVagasView.as_view(), name='pesquisa_vaga'),
]