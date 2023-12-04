from django.urls import path
from .views import login_view
from dashboard.views import dashboard  

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),  
]