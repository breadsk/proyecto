from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Carrito(models.Model):
    creado = models.DateTimeField(auto_now_add=True)



class ItemCarrito( models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

# Create your models here.
