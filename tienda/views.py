from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    context ={'productos': productos}
    return render (request, 'tienda/tienda.html', context)

def carrito(request):
    if request.user.is_authenticated :
        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
        items = orden.orderitem_set.all()
    else:
        items=[]
        orden = {'obtener_carrito_total':0, 'obtener_carrito_items':0}

    context ={'items' :items, 'orden':orden}
    return render (request, 'tienda/carrito.html', context)

def checkout(request):
    if request.user.is_authenticated :
        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
        items = orden.orderitem_set.all()
    else:
        items=[]
        orden = {'obtener_carrito_total':0, 'obtener_carrito_items':0}

    context ={'items' :items, 'orden':orden}
    return render (request, 'tienda/checkout.html', context)

def login(request,user):
    context ={}
    return render(request, 'registration/login.html', context)

def main (request):
    context = {}
    return render(request, 'tienda/main.html', context)

def registro(request):
    if request.method == 'POST':
        formulario = CustomerUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect('login')
    else:
        formulario = CustomerUserCreationForm()

    context = {'formulario': formulario}
    return render(request, 'registration/registro.html', context)