
from django.urls import path
from .views import lista, agregar_carrito, ver_carrito,eliminar

urlpatterns = [
    path('', lista, name='lista_productos'),
    path('agregar/<int:producto_id>', agregar_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar/<int:item_id>/', eliminar, name='eliminar_carrito'),
    
    
]