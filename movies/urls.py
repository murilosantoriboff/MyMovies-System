from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_detalhes/<int:id>/', views.ver_detalhes, name='ver_detalhes'),
    path('atualizar_filme/', views.atualizar_filme, name='atualizar_filme'),
    path('excluir_filme/<int:id>', views.excluir_filme, name='excluir_filme'),
    path('confirmar_exclusao/<int:id>', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('criar_filme/', views.criar_filme, name='criar_filme'),
    path('validacao_criacao_filmes/', views.validacao_criacao_filme, name='validacao_criacao_filme'),
]