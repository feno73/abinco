from django.urls import path
from . import views

app_name = 'inventario'
urlpatterns = [
    path('', views.pedidos, name='pedidos'),
]