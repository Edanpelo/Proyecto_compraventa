# Proyecto_compraventa

## Instalación

Es necesario contar con python3 y el paquete [pip](https://pip.pypa.io/en/stable/) para instalar los requerimientos: (en este proyecto se esta trabajando con la base de datos por defecto SQLite3 que no requiere instalación externa)

```bash
pip install -r requirements.txt
```

## Inizialización 

```bash
python manage.py makemigrations api_compraventa  # Crea nuevas modificaciones 
                                                 # basado en los modelos ubicados en api_compraventa.models
python manage.py migrate                         # Encargado de aplicar las migraciones
python manage.py sqlmigrate api_compraventa 0002 # Crea las sentencias SQL para una migración '0002' es la 
                                                 # ultima migracion de api_compraventa.migrations
python manage.py runserver
```
## Uso

Las urls que se utilizan en esta api son:

- ```http://127.0.0.1:8000/Clientes/``` con el metodo GET se ven todos los clientes y con el metodo POST se crea un nuevo cliente, es requerido enviar un texto en formato JSON como el siguiente:

{
    "nit":1118855062,
    "first_name": "Eddie",
    "last_name": "Perez",
    "address": "Una Direccion",
    "email": "eddielondoo@gmail.com",
    "phone": "1110001100"
}

- http://127.0.0.1:8000/Clientes/<int:nit> En esta url se aplican operaciones basicas del CRUD, GET <- consultar, PUT <- modificar, DELETE <- eliminar. En PUT es requerido enviar un texto en formato JSON como en el anterior item con la informacion modificada.

- http://127.0.0.1:8000/Clientes/<int:nit>/Compras En esta url se observa una lista de los productos comprados por el cliente.

- http://127.0.0.1:8000/Clientes/<int:nit>/Prendas En esta url se observa una lista de las prendas del cliente.

- http://127.0.0.1:8000/Articulos/ con el metodo GET se ven todos los articulos y con el metodo POST se crea un nuevo articulo, es requerido enviar un texto en formato JSON como el siguiente:

{
    "name": "Cadena lisa",
    "category": "Cadena"
    "price": 300000,
    "for_sale":0
}

- http://127.0.0.1:8000/Articulos/<int:pk> En esta url se aplican operaciones basicas del CRUD, GET <- consultar, PUT <- modificar, DELETE <- eliminar. En PUT es requerido enviar un texto en formato JSON como en el anterior item con la informacion modificada.





http://127.0.0.1:8000/En_venta/comprar
