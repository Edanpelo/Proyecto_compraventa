from django.urls import path
from api_compraventa import views

urlpatterns = [
    path('Clientes/', views.cliente_list),                      # Ver todos los clientes y crear nuevos clientes
    path('Clientes/<int:nit>', views.detalles_cliente),         # Operaciones basicas CRUD para el cliente
    path('Clientes/<int:nit>/Compras', views.compras_list),     # Lista productos comprados por cliente
    path('Clientes/<int:nit>/Prendas', views.prendas_cliente),  # Lista de prendas por cliente
    path('Articulos/', views.articulos_list),                   # Ver todos los articulos y crear nuevos articulos
    path('Articulos/<int:pk>', views.detalles_articulo),        # Operaciones basicas CRUD para el articulo
    path('En_venta/', views.en_venta_list),                     # Ver articulos en venta y comprar articulos
    path('Prendas/', views.prenda_list),                        # Ver todas las prendas y crear prendas
    # path('En_venta/comprar/', views.comprar_item),
    # path('Crear_prenda/<int:nit>/<int:pk>', views.crear_prenda),
]
