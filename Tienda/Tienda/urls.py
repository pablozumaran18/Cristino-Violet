from django.urls import path
from Ventas import views 
from django.contrib import admin
app_name = 'ventas'

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/',admin.site.urls, name='admin'),
    path('productos/', views.productos_list, name='productos_list'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('inicio/', views.inicio, name='inicio'),
]
