from django.urls import path
from . import views
urlpatterns =[
    path('', views.tienda, name ='tienda'),
    path('carrito/', views.carrito, name ='carrito'),
    path('checkout/', views.checkout, name ='checkout'),
    path('login/', views.login, name='login'),
    path('', views.main, name='main'),
    path('registro/', views.registro, name='registro' ),

]