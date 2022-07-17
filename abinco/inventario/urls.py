from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('productos/<int:id>/', views.detalle, name='detalle'),
    path('productos/<int:id>/actualizar/', views.actualizar, name='actualizar'),
]
