from django_countries.fields import CountryField
from django.db import models
from django.conf import settings

CHANNEL = (
    ("Online", "Online"),
    ("Offline", "Offline"),
)

PRIORITY = (
    ("H", "H"),
    ("C", "C"),
    ("L", "L"),
    ("M", "M"),
)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.


class Sale(models.Model):
    order_id = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    country = CountryField()
    itemType = models.ForeignKey(Category, on_delete=models.CASCADE)
    sales_channel = models.CharField(max_length=20, choices=CHANNEL)
    order_priority = models.CharField(max_length=20, choices=PRIORITY)
    order_date = models.DateField()
    ship_date = models.DateField()
    unit_sold = models.IntegerField()
    unit_price = models.FloatField()
    unit_cost = models.FloatField()

    @property
    def total_revenue(self):
        return round(self.unit_sold * self.unit_price, 2)

    @property
    def total_cost(self):
        return round(self.unit_sold * self.unit_cost,2)

    @property
    def total_profie(self):
        return round((self.unit_sold * self.unit_price) - (self.unit_sold * self.unit_cost), 2)

    def __str__(self):
        return str(self.order_id) + ' ' + self.itemType.name
