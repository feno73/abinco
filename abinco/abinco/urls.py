from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventario/", include('inventario.urls'), name='inventario'),
    path("pedidos/", include('pedidos.urls'), name='pedidos'),
    path('', include('cuentas.urls'), name='cuentas'),
]
