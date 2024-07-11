
from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto, Carrito, ItemCarrito


def lista(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'carritoApp/lista_productos.html', context)

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(id=request)
    request.session['carrito_id'] = carrito.id
    
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
    item.save()
    context ={}
    return render (request, 'carrito/ver_carrito.html', context)

def ver_carrito(request):
    carrito = Carrito.objects.all(id=request.session.get('carrito_id'))
    items = ItemCarrito.objects.filter(carrito=carrito)
    context = {'items':items}
    return render(request, 'carritoApp/ver_carrito.html', context)

def eliminar(request,item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')

