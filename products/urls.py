from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("<int:item_id>/", views.item, name='item'),
    path("services/<int:item_id>/", views.service_item, name='service_item'),
    path("purchase/", views.purchase, name='purchase'),
    path("cart/", views.cart, name='cart'),
    path("add_to_cart", views.add_to_cart, name='add_to_cart'),
    path("services/add_to_cart", views.service_add_to_cart, name='service_add_to_cart'),
    path("services/", views.services, name='services'),
    path("vendors/", views.vendors, name='vendors'),
    path("", views.products, name='products'),
]
