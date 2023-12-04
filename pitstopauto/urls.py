from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , include('login.urls')),
    path('clientes/', include('clientes.urls')),
    path('dashboard/', include('dashboard.urls')),  
    path('pecas/', include('pecas.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('servicos/', include('servicos.urls')),
    path('ordem_servico/', include('ordem_servico.urls')),
]