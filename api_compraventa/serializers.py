from rest_framework import serializers
from api_compraventa.models import Clientes, Articulos, Prendas, Vendidos


class ClientesSerializer(serializers.ModelSerializer):
    """ Modelo clientes serializados para comunicacion JSON """
    class Meta:
        model = Clientes
        fields = ['id', 'nit', 'first_name', 'last_name', 'address', 'email', 'phone']


class ArticulosSerializer(serializers.ModelSerializer):
    """ Modelo articulos serializados para comunicacion JSON """
    class Meta:
        model = Articulos
        fields = ['id', 'name', 'category', 'price', 'for_sale']


class PrendaSerializer(serializers.ModelSerializer):
    """ Modelo de prendas serializados para comunicacion JSON """
    class Meta:
        model = Prendas
        fields = ['id', 'garment_number', 'start_date', 'modified_date', 'expiration_date', 'interest_rate',
                  'capital_debt', 'debt', 'seller', 'item', 'expired']


class VendidosSerializer(serializers.ModelSerializer):
    """ Modelo de ventas serializadas para comunicacion JSON """
    class Meta:
        model = Vendidos
        fields = ['id', 'order_number', 'sale_date', 'buyer', 'sold_item']
