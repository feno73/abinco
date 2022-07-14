from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    busqueda = request.GET.get('buscarProducto')
    if busqueda:
        productos = Producto.objects.filter(codigo__icontains=busqueda)
    else:
        productos = Producto.objects.all()
    return render(request, 'home.html', {'busqueda':busqueda, 'productos':productos})

def detalle(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(request, 'detalle.html', {'producto':producto})
