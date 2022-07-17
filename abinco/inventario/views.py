from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Marca, Categoria, Ubicacion
from django.contrib.auth.decorators import login_required
from .forms import FormularioProducto
import logging

@login_required
def productos(request):
    busqueda = request.GET.get('buscarProducto')
    if busqueda:
        productos = Producto.objects.filter(codigo__icontains=busqueda)
    else:
        productos = Producto.objects.all()
    return render(request, 'inventario.html', {'busqueda':busqueda, 'productos':productos})

@login_required
def detalle(request, id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id)
        form = FormularioProducto(instance=producto)
        pk = id
        return render(request, 'detalle.html', {'form':form, 'pk':pk})


@login_required
def actualizar(request, id):
    producto = Producto.objects.get(id=id)
    producto.codigo = request.POST.get('codigo')
    producto.marca = Marca.objects.get(pk=request.POST.get('marca'))
    producto.categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
    producto.stock = request.POST.get('stock')
    producto.ubicacion = Ubicacion.objects.get(pk=request.POST.get('ubicacion'))
    producto.descripcion = request.POST.get('descripcion')
    producto.save()
    mensaje = "Se actualizó el registro"
    return redirect('detalle', id=id)

