from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Producto(models.Model):
        name = models.CharField(max_length=200, null=True)
        precio = models.FloatField(null=True)
        digital = models.BooleanField(default = False, null=True, blank=False)
        image= models.ImageField(null=True, blank=True)
        def __str__(self):
            return self.name

        @property
        def imageURL (self):
             try: 
                  url = self.image.url
             except:
                  url = ''
             return url 

class Orden(models.Model):
     cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
     date_orderd= models.DateTimeField(auto_now_add=True, null=True)
     complete = models.BooleanField( default=False, null=True, blank=False)
     transaction_id = models.CharField(max_length=100, null=True)

     def __str__(self):
        return str(self.id)
     
     @property
     def obtener_carrito_total(self):
          orderitems = self.orderitem_set.all()
          total = sum([item.obtener_total for item in orderitems])
          return total
     @property
     def obtener_carrito_items(self):
          orderitems = self.orderitem_set.all()
          total = sum([item.cantidad for item in orderitems])
          return total

class OrderItem (models.Model):
     producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
     orden = models.ForeignKey(Orden, on_delete=models.SET_NULL,  blank=True, null=True)
     cantidad = models.IntegerField(default=0, null=True, blank=True)
     date_added = models.DateField(auto_now_add=True)
     @property
     def obtener_total(self):
          total = self.producto.precio * self.cantidad
          return total

class ShippingAdress (models.Model):
     cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
     orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
     direccion = models.CharField(max_length=200, null=True)
     ciudad = models.CharField(max_length=200, null=True)
     estado = models.CharField(max_length=200, null=True)
     zipcode = models.CharField(max_length=200, null=True)
     date_added = models.DateField(auto_now_add=True)

     def __str__(self):
        return str(self.address)