from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('', views.listar_servicos, name='listar_servicos'),
    path('novo/', views.criar_servico, name='criar_servico'),
    path('editar/<int:id>/', views.editar_servico, name='editar_servico'),
    path('remover/<int:id>/', views.remover_servico, name='remover_servico'),
]   