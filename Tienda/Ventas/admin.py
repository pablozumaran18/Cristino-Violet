from django.contrib import admin
from .models import Producto, Carrito, CarritoItem

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
