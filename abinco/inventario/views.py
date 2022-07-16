from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.contrib.auth.decorators import login_required

@login_required
def productos(request):
    busqueda = request.GET.get('buscarProducto')
    if busqueda:
        productos = Producto.objects.filter(codigo__icontains=busqueda)
    else:
        productos = Producto.objects.all()
    return render(request, 'inventario.html', {'busqueda':busqueda, 'productos':productos})

@login_required
def detalle(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(request, 'detalle.html', {'producto':producto})
