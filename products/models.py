from pickle import FALSE
from turtle import screensize
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

class ProductType(models.TextChoices):
    PHONE = 'phone'
    TV = 'tv' 

class Product(models.Model):
    type = models.CharField(max_length=200, choices=[(tag, tag.value) for tag in ProductType], null=False)
    name = models.CharField(max_length=200, null=False)
    brand = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.CharField(max_length=200, null=False)
    size = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)],)
    shipping = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)
    
    class Meta:
        ordering = ('name', 'brand', 'size',)
    
class Cart(models.Model):
    customer = models.ForeignKey(User, verbose_name="customer", on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE, null=False)
    quantity = models.PositiveIntegerField(default=1, null=False)
    
    def __str__(self):
        return str(self.product) + " x " + str(self.quantity)
    
    class Meta:
       unique_together = ("customer", "product")