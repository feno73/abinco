from django.urls import path
from . import views

app_name = 'abinco_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<str:codigo>/', views.detalle, name='detalle'),
]
