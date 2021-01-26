# Proyecto_compraventa

## Instalación

Es necesario contar con python3 y el paquete [pip](https://pip.pypa.io/en/stable/) para instalar los requerimientos:

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
