from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuentas, name='cuentas'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('cerrarsesion/', views.cerrarsesion, name='cerrarsesion'),
]