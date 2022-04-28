from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path("<int:item_id>/", views.item, name='item'),
    path("purchase/", views.purchase, name='purchase'),
    path("cart/", views.cart, name='cart'),
    path("add_to_cart", views.add_to_cart, name='add_to_cart'),
    path("", views.products, name='products'),
]
