from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_compraventa.models import Clientes, Articulos, Prendas, Vendidos
from api_compraventa.serializers import ClientesSerializer, ArticulosSerializer, PrendaSerializer, VendidosSerializer
from datetime import datetime, timedelta


@api_view(['GET', 'POST'])
def cliente_list(request):
    """ Lista para ver todos los clientes o crear uno nuevo """
    if request.method == 'GET':             # Ver lista de todos los clientes
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':          # Crear un nuevo cliente
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def articulos_list(request):
    """ Lista para ver todos los articulos o crear uno nuevo """
    if request.method == 'GET':             # Ver lista de todos los articulos
        articulos = Articulos.objects.all()
        serializer = ArticulosSerializer(articulos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':          # Crear un nuevo articulo
        serializer = ArticulosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalles_cliente(request, nit):
    """ Leer, Actualizar o Borrar clientes """
    try:
        cliente = Clientes.objects.get(nit=nit)
    except Clientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':             # Leer un cliente con su NIT
        serializer = ClientesSerializer(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':           # Actualizar un cliente con su NIT
        serializer = ClientesSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':        # Borrar un cliente con su NIT
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def detalles_articulo(request, pk):
    """ Leer, Actualizar o Borrar articulos """
    try:
        articulo = Articulos.objects.get(pk=pk)
    except Articulos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':             # Leer un articulo con su id
        serializer = ArticulosSerializer(articulo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':           # Actualizar un articulo con su id
        serializer = ArticulosSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':        # Borrar un articulo con su id
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def en_venta_list(request):
    """ Lista para ver todos los articulos que se encuentran en venta y comprarlos """
    if request.method == 'GET':             # Ver todos los articulos en venta
        articulos = Articulos.objects.filter(for_sale=True)
        serializer = ArticulosSerializer(articulos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':          # Vender el articulo sold_item al comprador buyer
        serializer = VendidosSerializer(data=request.data)
        if serializer.is_valid():
            order_number = serializer.data.get('order_number')
            sale_date = serializer.data.get('sale_date')
            buyer = serializer.data.get('buyer')
            sold_item = serializer.data.get('sold_item')
            cliente = Clientes.objects.get(pk=buyer)
            articulo = Articulos.objects.get(pk=sold_item)
            venta = Vendidos.objects.create(order_number=order_number, sale_date=sale_date, buyer=cliente,
                                            sold_item=articulo)

            if articulo.for_sale is False:  # Filtro de validacion de compras
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                articulo.for_sale = False
                articulo.save()
                venta.save()
            serializer = VendidosSerializer(venta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def compras_list(request, nit):
    """ Ver lista de compras por cliente """
    try:
        cliente = Clientes.objects.get(nit=nit)
    except Clientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        venta = Vendidos.objects.filter(buyer=cliente)
        serializer = VendidosSerializer(venta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def prenda_list(request):
    """ Lista para ver todas las prendas y crearlas """
    if request.method == 'GET':             # Leer lista de todas las prendas
        prendas = Prendas.objects.all()
        serializer = PrendaSerializer(prendas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':          # Crear una nueva Prenda
        serializer = PrendaSerializer(data=request.data)
        if serializer.is_valid():
            garment_number = serializer.data.get('garment_number')
            start_date = serializer.data.get('start_date')
            modified_date = start_date
            expiration_date = datetime.strptime(modified_date, "%Y-%m-%d") + timedelta(days=180)
            expiration_date = expiration_date.date()
            interest_rate = serializer.data.get('interest_rate')
            seller = serializer.data.get('seller')
            item = serializer.data.get('item')
            cliente = Clientes.objects.get(pk=seller)
            articulo = Articulos.objects.get(pk=item)
            capital_debt = articulo.price
            debt = 0.0
            expired = False

            prenda = Prendas.objects.create(garment_number=garment_number, start_date=start_date,
                                            modified_date=modified_date, expiration_date=expiration_date,
                                            interest_rate=interest_rate, capital_debt=capital_debt, debt=debt,
                                            seller=cliente, item=articulo, expired=expired)

            if articulo.for_sale is True:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                prenda.save()
            serializer = PrendaSerializer(prenda)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def prendas_cliente(request, nit):
    """ Ver lista de prendas por cliente """
    try:
        cliente = Clientes.objects.get(nit=nit)
    except Clientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        prenda = Prendas.objects.filter(seller=cliente)
        serializer = PrendaSerializer(prenda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
