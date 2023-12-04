from django.urls import path
from .views import adicionar_mecanico, remover_mecanico, adicionar_mecanico_na_equipe, remover_mecanico_da_equipe, listar_mecanicos, listar_equipes, adicionar_equipe, detalhes_equipe, editar_mecanico, remover_equipe

app_name = 'funcionarios'

urlpatterns = [
    path('mecanico/adicionar/', adicionar_mecanico, name='adicionar_mecanico'),
    path('mecanico/editar/<int:mecanico_id>/', editar_mecanico, name='editar_mecanico'),
    path('mecanico/remover/<int:mecanico_id>/', remover_mecanico, name='remover_mecanico'),
    path('equipe/<int:equipe_id>/adicionar_mecanico/<int:mecanico_id>/', adicionar_mecanico_na_equipe, name='adicionar_mecanico_na_equipe'),
    path('equipe/<int:equipe_id>/remover_mecanico/<int:mecanico_id>/', remover_mecanico_da_equipe, name='remover_mecanico_da_equipe'),
    path('mecanicos/', listar_mecanicos, name='listar_mecanicos'),
    path('equipe/adicionar/', adicionar_equipe, name='adicionar_equipe'),
    path('equipe/<int:equipe_id>/', detalhes_equipe, name='detalhes_equipe'),
    path('equipe/remover/<int:equipe_id>/', remover_equipe, name='remover_equipe'),  # Nova rota para remover equipe
    path('', listar_equipes, name='listar_equipes'),
]