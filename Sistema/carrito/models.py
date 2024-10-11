from django.db import models
from Productos.models import Producto

class Carrito(models.Model);
    producto_id = models.ForeignKey(Producto,verbose_name="¨Producto ID", on_delete=models.CASCADE)

# Create your models here.
