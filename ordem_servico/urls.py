from django.urls import path
from . import views

app_name = 'ordem_servico'

urlpatterns = [
    path('', views.lista_ordens, name='lista_ordens'),
    path('criar/', views.criar_ordem, name='criar_ordem'),
    path('<int:id>/', views.detalhes_ordem, name='detalhes_ordem'),
    path('<int:id>/concluir/', views.concluir_ordem, name='concluir_ordem'),
    path('<int:id>/excluir/', views.excluir_ordem, name='excluir_ordem'),  # Adicione esta linha
]