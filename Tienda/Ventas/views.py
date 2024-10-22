from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, CarritoItem
from django.contrib import messages  # Para mostrar mensajes de error o éxito


def home(request):
    return render(request,'ventas/index.html')

# Vista para listar productos
def productos_list(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/productos_list.html', {'productos': productos})

# Vista para agregar productos al carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Verificar si el producto ya está en el carrito
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    print("carrito item ----------------------------->",carrito_item)
    if not created:
        carrito_item.cantidad += 1
    carrito_item.save()

    # Validar si se supera el stock disponible
    if carrito_item.cantidad + 1 > producto.stock:
        # Si no hay stock suficiente, mostrar mensaje de error
        messages.error(request, "No hay suficiente stock para agregar más de este producto.")
    else:
        # Si hay stock suficiente, incrementar la cantidad
        carrito_item.cantidad += 1
        carrito_item.save()
        messages.success(request, "Producto agregado al carrito.")

#Redireccion al carrito
    return redirect('carrito')

# Vista para ver el carrito
@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    print('carrito-------------------------->', carrito)
    items = CarritoItem.objects.get(carrito = carrito)
    print('items---------------------------->', items)
    return render(request, 'ventas/carrito.html', {'carrito': carrito})


def about(request):
    return render(request, 'ventas/about.html')

def contact(request):
    return render(request, 'ventas/contact.html')


def eliminar_del_carrito(request, producto_id):
    carrito = Carrito.objects.get(usuario=request.user)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item = CarritoItem.objects.get(carrito=carrito, producto=producto)

    if carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
        messages.success(request, "Producto eliminado correctamente.")
    else:
        # Si la cantidad es 1, eliminar el ítem completamente
        carrito_item.delete()
        messages.success(request, "Producto eliminado del carrito.")

    return redirect('ventas:carrito')


def inicio(request):
    return render(request, 'ventas/inicio.html')