from django.db import models


class Clientes(models.Model):
    """ Modelo de clientes """
    nit = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Articulos(models.Model):
    """ Modelo de artículos """
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    for_sale = models.BooleanField()

    def __str__(self):
        return 'name: %s, category: %s, price: %s, for_sale: %s' % (self.name, self.category, self.price, self.for_sale)


class Prendas(models.Model):
    """ Modelo de prendas"""
    garment_number = models.IntegerField(unique=True)
    start_date = models.DateField(null=True, blank=True)
    modified_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    interest_rate = models.FloatField(default=0.1)
    capital_debt = models.FloatField(null=True, blank=True)
    debt = models.FloatField(null=True, blank=True)
    seller = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    item = models.ForeignKey(Articulos, on_delete=models.PROTECT)
    expired = models.BooleanField(default=False)


class Vendidos(models.Model):
    """ Articulos vendidos """
    order_number = models.IntegerField(unique=True)
    sale_date = models.DateField()
    buyer = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    sold_item = models.ForeignKey(Articulos, on_delete=models.PROTECT)
