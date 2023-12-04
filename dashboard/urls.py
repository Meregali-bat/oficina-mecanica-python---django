from django.urls import path
from .views import dashboard
from django.contrib import admin
from django.urls import include, path

app_name = 'dashboard'  

urlpatterns = [
    path('', dashboard, name='dashboard'), 
    path('clientes/', include('clientes.urls')),
]