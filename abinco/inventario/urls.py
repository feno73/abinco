from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('productos/<str:codigo>/', views.detalle, name='detalle'),
]
