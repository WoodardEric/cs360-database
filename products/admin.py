from django.contrib import admin

from .models import ProductType, Vendor, Product, Cart, Service

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Service)
