from enum import Enum, IntEnum
from pickle import FALSE
from django.db import models

class ProductType(models.TextChoices):
    PHONE = 'phone'
    TV = 'tv' 

class Product(models.Model):
    type = models.CharField(max_length=200, choices=[(tag, tag.value) for tag in ProductType], null=False)
    name = models.CharField(max_length=200, null=False)
    brand = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)