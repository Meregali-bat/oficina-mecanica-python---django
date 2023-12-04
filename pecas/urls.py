from django.urls import path
from .views import adicionar_peca, listar_pecas, remover_peca

app_name = 'pecas'

urlpatterns = [
    path('', listar_pecas, name='listar_pecas'),
    path('adicionar/', adicionar_peca, name='adicionar_peca'),
    path('remover/<int:peca_id>/', remover_peca, name='remover_peca'),
]